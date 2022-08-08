from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as mplt
from sklearn.cluster import KMeans

image = mplt.imread("image.jpg")
mplt.imshow(image)
mplt.axis('off')
mplt.show()

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

varLen = kmeans.predict(image_array)

print(kmeans.cluster_centers_)
e = kmeans.cluster_centers_


def createImage(c, varLen, w, h, d):
    image = np.zeros((w, h, d))
    label_idx=0

    for i in range(w):
        for j in range(h):
            image[i][j] = c[varLen[label_idx]]
            label_idx+=1
    
    return image


mplt.figure(1)
mplt.axis('off')
mplt.title("original")
mplt.imshow(image)
mplt.show()
mplt.figure(2)
mplt.axis('off')
mplt.title("reduced")
mplt.imshow(createImage(e,varLen,w,h,d))
mplt.show()