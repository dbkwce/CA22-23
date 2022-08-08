from skimage import io
from sklearn.cluster import KMeans
import numpy as np

image = io.imread('shiva.png')
io.imshow(image)
io.show()

rows = image.shape[0]
cols = image.shape[1]

image = image.reshape(rows*cols, 4)

kmeans = KMeans(n_clusters=64)
kmeans.fit(image)

compressed_image = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = np.clip(compressed_image.astype('uint8'), 0, 128)

compressed_image = compressed_image.reshape(rows, cols, 4)

io.imsave('compressed_shiva.png', compressed_image)
io.imshow(compressed_image)
io.show()