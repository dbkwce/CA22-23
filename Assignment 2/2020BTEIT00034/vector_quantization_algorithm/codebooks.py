import random
import numpy as np


def random_codebook(vectors, length=512, seed=None):
    if seed is not None:
        random.seed(seed)
    codebook = random.sample(np.unique(vectors, axis=0).tolist(), length)
    # Following line is 2 times faster but creates codebook with possible duplicates
    # codebook = random.sample(vectors.tolist(), length)
    return np.array(codebook)
