"""
Name : Harshali Laxmikant Parihar.
PRN : 2020BTEIT00030
Program : Vector Quantization for Image Compression

"""

import numpy as np
import scipy as sp
# For plotting and Visualization
import matplotlib.pyplot as plt

from sklearn import cluster

from PIL import Image

im = Image.open("Image.png")
im = np.array(im)


n_clusters = 5
np.random.seed(0)

X = im.reshape((-1, 1))  
k_means = cluster.KMeans(n_clusters=n_clusters, n_init=4)
k_means.fit(X)
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_

# create an array from labels and values
im_compressed = np.choose(labels, values)
im_compressed.shape = im.shape

vmin = im.min()
vmax = im.max()

# original image
plt.figure(1, figsize=(3, 2.2))
plt.imshow(im.astype('uint8'), cmap=plt.cm.gray, vmin=vmin, vmax=256, )

# compressed image
plt.figure(2, figsize=(3, 2.2))
plt.imshow(im_compressed.astype('uint8'),
           cmap=plt.cm.gray, vmin=vmin, vmax=vmax, )
Image.fromarray((im_compressed).astype("uint8")).save("compressed.png")


plt.show() 