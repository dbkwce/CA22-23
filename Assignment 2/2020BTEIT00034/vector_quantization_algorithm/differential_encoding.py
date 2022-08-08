import numpy as np


def differential_encoding(image):
    image = image.astype("float64")
    height, width = image.shape
    encoded = np.zeros(image.shape, dtype="float64")
    # rewrite first element
    encoded[0, 0] = image[0, 0]
    # calculate first row
    for i in range(1, width):
        encoded[0, i] = image[0, i] - image[0, i - 1]
    # calculate first column
    for i in range(1, height):
        encoded[i, 0] = image[i, 0] - image[i - 1, 0]
    # calculate other values
    for i in range(1, height):
        for j in range(1, width):
            encoded[i, j] = image[i, j] - image[i, j - 1]
    return encoded


def differential_decoding(codes):
    codes = codes.astype("float64")
    height, width = codes.shape
    image = np.zeros(codes.shape, dtype="float64")
    # rewrite first element
    image[0, 0] = codes[0, 0]
    # calculate first row
    for i in range(1, width):
        image[0, i] = codes[0, i] + image[0, i - 1]
    # calculate first column
    for i in range(1, height):
        image[i, 0] = codes[i, 0] + image[i - 1, 0]
    # calculate other values
    for i in range(1, height):
        for j in range(1, width):
            image[i, j] = codes[i, j] + image[i, j - 1]
    return image


def differential_median_encoding(image):
    image = image.astype("float64")
    height, width = image.shape
    encoded = np.zeros(image.shape, dtype="float64")
    # rewrite first element
    encoded[0, 0] = image[0, 0]
    # calculate first row
    for i in range(1, width):
        encoded[0, i] = image[0, i] - image[0, i - 1]
    # calculate first column
    for i in range(1, height):
        encoded[i, 0] = image[i, 0] - image[i - 1, 0]
    # calculate other values
    for i in range(1, height):
        for j in range(1, width):
            encoded[i, j] = image[i, j] - np.mean([image[i, j - 1], image[i - 1, j], image[i - 1, j - 1]])
    return encoded


def differential_median_decoding(codes):
    codes = codes.astype("float64")
    height, width = codes.shape
    image = np.zeros(codes.shape, dtype="float64")
    # rewrite first element
    image[0, 0] = codes[0, 0]
    # calculate first row
    for i in range(1, width):
        image[0, i] = codes[0, i] + image[0, i - 1]
    # calculate first column
    for i in range(1, height):
        image[i, 0] = codes[i, 0] + image[i - 1, 0]
    # calculate other values
    for i in range(1, height):
        for j in range(1, width):
            image[i, j] = codes[i, j] + np.mean([image[i, j - 1], image[i - 1, j], image[i - 1, j - 1]])
    return image


def median_adaptive_predictor_encoding(image):
    """
    Using median edge detector - nonlinear predictor
    """
    image = image.astype("float64")
    height, width = image.shape
    encoded = np.zeros(image.shape, dtype="float64")
    # rewrite first element
    encoded[0, 0] = image[0, 0]
    # calculate first row
    for i in range(1, width):
        encoded[0, i] = image[0, i] - image[0, i - 1]
    # calculate first column
    for i in range(1, height):
        encoded[i, 0] = image[i, 0] - image[i - 1, 0]
    # calculate other values
    for i in range(1, height):
        for j in range(1, width):
            p1 = image[i, j - 1]
            p2 = image[i - 1, j]
            p3 = image[i - 1, j - 1]
            if p1 > p2:
                x_max = p1
                x_min = p2
            else:
                x_max = p2
                x_min = p1
            if p3 >= x_max:
                # context 1 as described in Entropia_2.doc
                x_med = min(p1, p2)
            elif p3 <= x_min:
                # context 2
                x_med = max(p1, p2)
            else:
                # context 3
                x_med = p1 + p2 - p3
            encoded[i, j] = image[i, j] - x_med
    return encoded


def median_adaptive_predictor_decoding(codes):
    """
    Using median edge detector - nonlinear predictor
    """
    codes = codes.astype("float64")
    height, width = codes.shape
    image = np.zeros(codes.shape, dtype="float64")
    # rewrite first element
    image[0, 0] = codes[0, 0]
    # calculate first row
    for i in range(1, width):
        image[0, i] = codes[0, i] + image[0, i - 1]
    # calculate first column
    for i in range(1, height):
        image[i, 0] = codes[i, 0] + image[i - 1, 0]
    # calculate other values
    for i in range(1, height):
        for j in range(1, width):
            # image[i, j] = codes[i, j] + np.mean([image[i, j - 1], image[i - 1, j], image[i - 1, j - 1]])
            p1 = image[i, j - 1]
            p2 = image[i - 1, j]
            p3 = image[i - 1, j - 1]
            if p1 > p2:
                x_max = p1
                x_min = p2
            else:
                x_max = p2
                x_min = p1
            if p3 >= x_max:
                # context 1 as described in Entropia_2.doc
                x_med = min(p1, p2)
            elif p3 <= x_min:
                # context 2
                x_med = max(p1, p2)
            else:
                # context 3
                x_med = p1 + p2 - p3
            image[i, j] = codes[i, j] + x_med
    return image


if __name__ == "__main__":
    from PIL import Image

    from vector_quantization.metrics import PSNR
    from vector_quantization.image import load_image, save_image
    from vector_quantization.codebooks import random_codebook
    from vector_quantization.vectorize import vectorize, image_from_vectors
    from vector_quantization.lbg import lbg
    from vector_quantization.mean_removal_quantization import mean_removal_quantize
    from vector_quantization.mean_removal_quantization import mean_removal_quantize_from_codebook

    import matplotlib.pyplot as plt

    img = load_image("lennagrey.bmp")

    # Performing quantization with removed means (MRVQ)
    window_size = 4
    vectors = vectorize(img, window_size=window_size)
    means = np.mean(vectors, axis=1, keepdims=True)  # mean should be in shape like smaller image.
    height, width = img.shape
    means_reshaped = means.reshape((height // window_size, width // window_size))

    # Differential encoding means from MRVQ
    encoded = differential_encoding(means_reshaped)

    # Show encoded image
    plt.imshow(encoded)
    plt.show()

    # Make histograms with probability
    hist_means, bins_means = np.histogram(means, bins=np.arange(256))
    hist_means = hist_means / np.sum(hist_means)
    hist_encoded, bins_encoded = np.histogram(encoded.ravel(), bins=np.arange(-255, 256))
    hist_encoded = hist_encoded / np.sum(hist_encoded)
    plt.plot(bins_means[:-1], hist_means, label="Średnie bloków")
    plt.plot(bins_encoded[:-1], hist_encoded, label="Kodowanie różnicowe")
    plt.legend()
    plt.show()

    # Calculate entropy
    from scipy.stats import entropy

    entropy_means = entropy(hist_means, base=2)
    entropy_encoded = entropy(hist_encoded, base=2)
    print(f"Entropia średnie = {entropy_means}, entropia kodowanie różnicowe = {entropy_encoded}")
