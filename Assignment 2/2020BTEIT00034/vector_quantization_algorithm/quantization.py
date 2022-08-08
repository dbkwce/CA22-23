import numpy as np
import timeit
from scipy.cluster.vq import vq

from vector_quantization_algorithm.vectorize import vectorize, image_from_vectors


def quantize(image, window_size, codebook_fun, codebook_size, verbose=False):
    print("Quantizing image...")

    quantized_img = image.copy()
    vectors = vectorize(quantized_img, window_size=window_size)
    codebook = codebook_fun(vectors, length=codebook_size)

    quantized_vectors = quantize_from_codebook(vectors, codebook)

    quantized_img = image_from_vectors(quantized_vectors, quantized_img)
    return quantized_img


def quantize_from_codebook(vectors, codebook):
    print("Quantizing vectors...")

    # TODO: maybe add return codes?
    quantized_vectors = np.zeros_like(vectors)
    codes, _ = vq(vectors, codebook)
    for idx, vector in enumerate(vectors):
        quantized_vectors[idx, :] = codebook[codes[idx], :]
    return quantized_vectors


def codes_from_vectors(vectors, codebook):
    print("Quantizing vectors...")

    codes, _ = vq(vectors, codebook)
    return codes


def vectors_from_codes(codes, codebook):
    print("Quantizing vectors...")

    vectors = [codebook[code] for code in codes]
    return np.array(vectors)


if __name__ == "__main__":
    print("Quantization script started.")

    from PIL import Image
    from metrics import PSNR
    from image import load_image, save_image
    from codebooks import random_codebook

    img = load_image("Daulatrao-Patil-BW.bmp")
    quantized_img = quantize(img, window_size=4, codebook_fun=random_codebook, codebook_size=32)
    print("PSNR:", PSNR(img, quantized_img))
    Image.fromarray(quantized_img).show()
