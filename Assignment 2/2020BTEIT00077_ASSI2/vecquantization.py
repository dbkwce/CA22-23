import numpy as np
import scipy as sp
import matplotlib.pyplot as plot

from sklearn import cluster

from PIL import Image

img = Image.open("Abhi.jpeg")
img = np.array(img)


n_clusters = 5
np.random.seed(0)

X = img.reshape((-1, 1))  
k_means = cluster.KMeans(n_clusters=n_clusters, n_init=4)
k_means.fit(X)
values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_

# array from labels and values
img_compressed = np.choose(labels, values)
img_compressed.shape = img.shape

vmin = img.min()
vmax = img.max()

#inputted uncompressed image
plot.figure(1, figsize=(3, 2.2))
plot.imshow(img.astype('uint8'), cmap=plot.cm.gray, vmin=vmin, vmax=256, )

# compressed image
plot.figure(2, figsize=(3, 2.2))
plot.imshow(img_compressed.astype('uint8'),
           cmap=plot.cm.gray, vmin=vmin, vmax=vmax, )
Image.fromarray((img_compressed).astype("uint8")).save("compressed.png")


plot.show() 