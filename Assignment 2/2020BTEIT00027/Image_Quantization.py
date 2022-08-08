"""
Name : Aditi Jitendra Sawant
PRN : 2020BTEIT00027
Program : Vector Quantization for Image Compression

"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from sklearn import cluster

from PIL import Image

pic = Image.open("Img/Nature.png")
pic = np.array(pic)


n_clusters = 5
np.random.seed(0)

X = pic.reshape((-1, 1))
k_means_cluster = cluster.KMeans(n_clusters=n_clusters, n_init=4)
k_means_cluster.fit(X)
values = k_means_cluster.cluster_centers_.squeeze()
labels = k_means_cluster.labels_

pic_compressed = np.choose(labels, values)
pic_compressed.shape = pic.shape

vmin = pic.min()
vmax = pic.max()

plt.figure(1, figsize=(3, 2.2))
plt.imshow(pic.astype('uint8'), cmap=plt.cm.gray, vmin=vmin, vmax=256, )

plt.figure(2, figsize=(3, 2.2))
plt.imshow(pic_compressed.astype('uint8'),
           cmap=plt.cm.gray, vmin=vmin, vmax=vmax, )
Image.fromarray((pic_compressed).astype("uint8")).save("output.png")


plt.show()
