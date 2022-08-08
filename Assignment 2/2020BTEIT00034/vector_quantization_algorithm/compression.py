"""
End to end compression script
"""
import numpy as np
from PIL import Image
from bitarray import bitarray
from bitarray.util import ba2int, int2ba

from vector_quantization.image import load_image, save_image
from vector_quantization.metrics import PSNR
from vector_quantization.codebooks import random_codebook
from vector_quantization.vectorize import vectorize, image_from_vectors
from vector_quantization.quantization import quantize, quantize_from_codebook, vectors_from_codes
from vector_quantization.lbg import lbg
from vector_quantization.mean_removal_quantization import mean_removal_quantize_from_codebook
from vector_quantization.differential_encoding import (
    median_adaptive_predictor_encoding,
    median_adaptive_predictor_decoding,
)
from vector_quantization.golomb_coder import golomb_compress, golomb_decompress


def compression(img, codebook_size=2 ** 10, window_size=4):
    vectors = vectorize(img, window_size=window_size)
    means = np.mean(vectors, axis=1, keepdims=True)
    residual_vectors = vectors - means
    initial_codebook = random_codebook(residual_vectors, length=codebook_size)
    codebook, _ = lbg(residual_vectors, initial_codebook, 50, 0.01)
    _, (codes, _) = mean_removal_quantize_from_codebook(residual_vectors, means, codebook)

    codebook_bitcode = codebook_compression(img.shape, window_size, codes, codebook)
    means_bitcode = means_compression(img.shape, window_size, means)
    bitcode = codebook_bitcode + means_bitcode

    return bitcode


def codebook_compression(image_shape, window_size, codes, codebook):
    height, width = image_shape

    res = bitarray()

    height_code = f"{int(height):032b}"
    width_code = f"{int(width):032b}"
    res += bitarray(height_code)
    res += bitarray(width_code)

    window_size_code = f"{int(window_size):032b}"
    res += bitarray(window_size_code)

    codebook_size = len(codebook)
    codebook_size_code = f"{int(codebook_size):032b}"
    res += bitarray(codebook_size_code)

    for codebook_code in codebook:
        for element in codebook_code:
            element_code = int2ba(int(element), length=9, signed=True)
            res += element_code

    bits_per_code = int(np.ceil(np.log2(codebook_size)))
    for vector_code in codes:
        vector_code_code = int2ba(int(vector_code), length=bits_per_code, signed=False)
        res += vector_code_code

    return res


def means_compression(image_shape, window_size, means):
    height, width = image_shape

    # Means reshaping for differential encoding
    means_reshaped = means.reshape((height // window_size, width // window_size))
    means_reshaped = means_reshaped.astype(int)

    # Differential encoding means
    encoded_means = median_adaptive_predictor_encoding(means_reshaped)
    encoded_means = encoded_means.astype(int)

    # Compress encoded means with Golomb Coder
    bit_code = golomb_compress(encoded_means)

    return bit_code


def decompression(bitcode):
    img_shape, window_size, codes, codebook, ptr = codebook_decompression(bitcode)

    # Recreate residual vectors from codebook
    residual_vectors = vectors_from_codes(codes, codebook)

    # Means decompression (golomb decompression and differential decoding)
    means_bitcode = bitcode[ptr:]
    means = means_decompression(means_bitcode, window_size)

    # Recreating vectors from residual vectors and means
    vectors = residual_vectors + means

    img_tmp = np.zeros(img_shape)

    img = image_from_vectors(vectors, img_tmp)
    return img


def codebook_decompression(codebook_bitcode):
    # height, width
    ptr = 32
    size_h_code = codebook_bitcode[0:ptr]
    size_w_code = codebook_bitcode[ptr : ptr + 32]
    ptr += 32
    img_shape = [int(size_h_code.to01(), 2), int(size_w_code.to01(), 2)]

    # window_size
    window_size_code = codebook_bitcode[ptr : ptr + 32]
    ptr += 32
    window_size = int(window_size_code.to01(), 2)

    # codebook
    codebook_size_code = codebook_bitcode[ptr : ptr + 32]
    ptr += 32
    codebook_size = int(codebook_size_code.to01(), 2)
    codebook = []
    for i in range(codebook_size):
        codebook_element = []
        for j in range(window_size ** 2):
            value_code = codebook_bitcode[ptr : ptr + 9]
            ptr += 9
            value = ba2int(value_code, signed=True)
            codebook_element.append(value)
        codebook.append(codebook_element)
    codebook = np.array(codebook)

    # codes
    codes_size = int((img_shape[0] * img_shape[1]) / (window_size ** 2))
    bits_per_code = int(np.ceil(np.log2(codebook_size)))

    codes = []
    for i in range(codes_size):
        value_code = codebook_bitcode[ptr : ptr + bits_per_code]
        ptr += bits_per_code
        code = ba2int(value_code, signed=False)
        codes.append(code)
    codes = np.array(codes)

    return img_shape, window_size, codes, codebook, ptr


def means_decompression(means_bitcode, window_size):
    # Decompress encoded means with Golomb Coder
    encoded_means = golomb_decompress(means_bitcode)

    # Differential decoding
    means_reshaped = median_adaptive_predictor_decoding(encoded_means)
    means = means_reshaped.reshape(-1, 1)

    return means


def to_file(img, file_path):
    bitcode = compression(img)
    f = open(file_path, "wb")
    bitcode.tofile(f)
    f.close()


def from_file(file_path):
    f = open(file_path, "rb")
    bitcode = bitarray()
    bitcode.fromfile(f)
    f.close()

    img = decompression(bitcode)
    return img


if __name__ == "__main__":
    # with file
    img = load_image("balloon.bmp")
    file_path = "./img/output/balloon.vc"
    to_file(img, file_path)
    out_img = from_file(file_path)

    print("PSNR:", PSNR(img, out_img))
    Image.fromarray(out_img).show()

    # without file
    img = load_image("balloon.bmp")
    bitcode = compression(img)
    out_img = decompression(bitcode)

    print("PSNR:", PSNR(img, out_img))
    print("bit_code length", len(bitcode))
    print("without compression", img.size * 8)
    print("CR", len(bitcode) / (img.size * 8))
    Image.fromarray(out_img).show()
