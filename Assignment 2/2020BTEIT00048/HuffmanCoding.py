from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = plt.imread("flower.jpg")
plt.imshow(image)
plt.axis('off')
plt.show()

type(image)

print(image.shape)
print(image.size)

w, h, d = image.shape
image_array = image.reshape(w*h, d)
print(image_array.shape)

image_array = image_array/255
array_sample = shuffle(image_array, random_state=1)[:2000]
array_sample.size

kmeans = KMeans(n_clusters=6, random_state=1)
kmeans.fit(array_sample)

varL = kmeans.predict(image_array)

print(kmeans.cluster_centers_)
e = kmeans.cluster_centers_


def createImage(c, varL, w, h, d):
    image = np.zeros((w, h, d))
    label_idx=0

    for i in range(w):
        for j in range(h):
            image[i][j] = c[varL[label_idx]]
            label_idx+=1

    return image


plt.figure(1)
plt.axis('off')
plt.title("original")
plt.imshow(image)
plt.show()
plt.figure(2)
plt.axis('off')
plt.title("reduced")
plt.imshow(createImage(e,varL,w,h,d))
plt.show()