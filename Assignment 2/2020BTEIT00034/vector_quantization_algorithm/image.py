"""
Loading and saving image files.
"""
from PIL import Image
import numpy as np
import os


def load_image(file_name, path=None):
    print("Loading image:", file_name)

    if path is None:
        img = Image.open("./img/input/" + file_name)
    else:
        img = Image.open(path + file_name)
    img_arr = np.array(img)
    return img_arr


def save_image(img_arr, file_name):
    print("Saving image:", file_name)

    img = Image.fromarray(img_arr)
    path = "./img/output/"
    os.mkdir(path)
    img.save("./img/output/" + file_name + "Compressed.bmp")
