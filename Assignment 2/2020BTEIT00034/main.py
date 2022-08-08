"""
Assignment 2 : Vector Quantization
Daulatrao Patil : 2020BTEIT00034
Monday: 08/08/2022
"""
from PIL import Image

from vector_quantization_algorithm.metrics import PSNR
from vector_quantization_algorithm.image import load_image, save_image
from vector_quantization_algorithm.codebooks import random_codebook
from vector_quantization_algorithm.vectorize import vectorize, image_from_vectors
from vector_quantization_algorithm.quantization import quantize, quantize_from_codebook
from vector_quantization_algorithm.lbg import lbg

if __name__ == "__main__":
    # Load image
    img = load_image("Daulatrao-Patil-BW-Reszied.bmp")

    # Quantize image
    vectors = vectorize(img, window_size=4)
    
    # Create codebook
    initial_codebook = random_codebook(vectors, length=32)
    
    # Quantize vectors
    codebook, distortions = lbg(vectors, initial_codebook, 50, 0.01)
    
    # Quantize vectors 
    quantized_img_lbg = image_from_vectors(quantize_from_codebook(vectors, codebook), img.copy())
    
    # Save image
    Image.fromarray(quantized_img_lbg).show()

    print(codebook)
    print(distortions)
