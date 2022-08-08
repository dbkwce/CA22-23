import numpy as np


def vectorize(img, window_size):
    """
    Slice image into blocks of size window_size and flatten them.

    Check this diagram: https://i.imgur.com/wycSwR3.png

    Args:
        img: numpy array with image values
        window_size: size of window. Length of vectors will be window_size ** 2
    """

    print("Vectorizing image...")
    print(img.shape)
    height, width = img.shape[0], img.shape[1]
    if height % window_size != 0 or width % window_size != 0:
        raise ValueError(f"Dimension of input image ({img.shape}) must be divided by {window_size}.")

    num_of_vectors = height // window_size * width // window_size
    vectors = np.zeros((num_of_vectors, window_size ** 2))

    index = 0
    ws = window_size
    for i in range(height // ws):
        for j in range(width // ws):
            vectors[index, :] = img[i * ws : i * ws + ws, j * ws : j * ws + ws].flat
            index += 1

    return vectors


def image_from_vectors(vectors, image):
    print("Reconstructing image...")

    height, width = image.shape
    index = 0
    ws = int(np.sqrt(vectors[0].size))
    for i in range(height // ws):
        for j in range(width // ws):
            image[i * ws : i * ws + ws, j * ws : j * ws + ws].flat = vectors[index, :]
            index += 1
    return image


if __name__ == "__main__":
    print("Vectorization script started.")

    from image import load_image

    img = load_image("balloon.bmp")
    vectors = vectorize(img, 2)
    print(vectors)
