import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


img = plt.imread("ORIGINAL.jpeg")
plt.imshow(img)
plt.axis('off')
plt.show()

type(img)

print(img.shape)
print(img.size)


w,h, d = img.shape
# d=1
image_array = img.reshape(w*h, d)
print(image_array.shape)

#normalize in the range of (0,1)

image_array=image_array/255


from sklearn.utils import shuffle
# fitting model on a small sub sample of the complete image
image_array_sample =shuffle(image_array, random_state=1)[:1000]
image_array_sample.size

kmeans =KMeans(n_clusters=6, random_state=1)
kmeans.fit(image_array_sample)

labels=kmeans.predict(image_array)
labels

print(kmeans.cluster_centers_)
c=kmeans.cluster_centers_


# recreate original image according to labes and each pixels

def recreate_image(c,labels,w,h,d):
  image=np.zeros((w,h,d))
  label_idx =0

#now label each pixels according to the limited labels


  for i in range(w):
    for j in range(h):
      image[i][j]=c[labels[label_idx]]
      label_idx +=1

  return(image)

plt.figure(1)
plt.axis('off')
plt.title("original")
plt.imshow(img)
plt.show()
plt.figure(2)
plt.axis('off')
plt.title("reduced")
plt.imshow(recreate_image(c,labels,w,h,d))
plt.show()
