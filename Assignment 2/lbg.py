import numpy as np
from scipy.spatial import distance
from scipy.cluster.vq import vq


def lbg(vectors, initial_codebook, iterations, error=None):
    m = 1
    distortions = [np.inf]
    finished = False
    code_book = initial_codebook
    cb_length = code_book.shape[0]

    while not finished and m < iterations:
        # Assign each vector to cluster
        codes, dists = vq(vectors, code_book)
        # Calculate mean distortion
        distortions.append(np.mean(dists))
        # Find new centroids
        for i in range(cb_length):
            code_book[i, :] = np.mean(vectors[codes == i], axis=0)
        # Check condition if gain of distortion is small
        distortion_difference = (distortions[m - 1] - distortions[m]) / distortions[m]
        # print(f"lbg iteration: {m}, distortion: {distortions[-1]}, diff: {distortion_difference}")
        if error is not None:
            if distortion_difference < error:
                finished = True
        m += 1

    return code_book.astype("int32"), distortions


if __name__ == "__main__":
    from vector_quantization.quantization import codes_from_vectors, vectors_from_codes

    # Create codebook and codes
    vectors = np.array([[1, 1], [2, 2], [1, 1], [3, 3], [4, 4], [1, 1]])
    initial_codebook = np.array([[1, 1], [2, 2]])
    codebook, _ = lbg(vectors, initial_codebook, iterations=50, error=0.0)
    codes = codes_from_vectors(vectors, codebook)

    # From codebook and codes create vectors and then image
    quantized_vectors = vectors_from_codes(codes, codebook)

    print(quantized_vectors)
    print(codebook)
