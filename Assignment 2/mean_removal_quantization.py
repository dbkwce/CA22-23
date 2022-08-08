from PIL import Image

from vector_quantization.metrics import PSNR
from vector_quantization.image import load_image, save_image
from vector_quantization.codebooks import random_codebook
from vector_quantization.vectorize import vectorize, image_from_vectors
from vector_quantization.quantization import quantize, quantize_from_codebook
from vector_quantization.lbg import lbg

import numpy as np
from scipy.cluster.vq import vq


def mean_removal_quantize(image, window_size, codebook_fun, codebook_size, verbose=False):
    quantized_img = image.copy()
    vectors = vectorize(quantized_img, window_size=window_size)
    means = np.mean(vectors, axis=1, keepdims=True)
    residual_vectors = vectors - means
    initial_codebook = codebook_fun(residual_vectors, length=codebook_size)
    codebook, distortions = lbg(residual_vectors, initial_codebook, 50, 0.01)
    quantized_vectors, (codes, _) = mean_removal_quantize_from_codebook(residual_vectors, means, codebook), img.copy()
    quantized_img = image_from_vectors(quantized_vectors)
    return quantized_img, (codes, means)


def mean_removal_quantize_from_codebook(vectors, means, codebook):
    quantized_vectors = np.zeros_like(vectors)
    codes, _ = vq(vectors, codebook)
    for idx, vector in enumerate(vectors):
        quantized_vectors[idx, :] = codebook[codes[idx], :] + means[idx]
    return quantized_vectors, (codes, means)


if __name__ == "__main__":
    img = load_image("balloon.bmp")
    vectors = vectorize(img, window_size=4)
    means = np.mean(vectors, axis=1, keepdims=True)
    residual_vectors = vectors - means
    initial_codebook = random_codebook(residual_vectors, length=32)
    codebook, distortions = lbg(residual_vectors, initial_codebook, 50, 0.01)
    quantized_vectors, (codes, _) = mean_removal_quantize_from_codebook(residual_vectors, means, codebook)
    quantized_img_lbg = image_from_vectors(quantized_vectors, img.copy())

    print("PSNR:", PSNR(img, quantized_img_lbg))
    Image.fromarray(quantized_img_lbg).show()
