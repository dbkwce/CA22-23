"""
All metrics used to compare images.
"""
import numpy as np
import math


def PSNR(original_image, referenced_image):
    mse = np.mean((original_image - referenced_image) ** 2)
    if mse == 0:  # MSE is zero means no noise is present in the signal .
        # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr
