#----------------------------------------------

# Om Vivek Gharge
# PRN: 2020BTEIT00041

# Assignment 2: Vector Quantization

#----------------------------------------------

import numpy as np
import pandas as pd
import sklearn 
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import decomposition as dcmp
from sklearn import preprocessing as prep
from sklearn import cluster
import matplotlib.image as mpimg
from skimage.io import imread, imshow, imsave
import os

#Loading the data
dtu=imread("original.jpg")

# Making the image compatible with matplotlib 
# Matplotlib represent RGB from value 0 to 1
dtu_f64=dtu.astype(dtype=np.float64)/255

# Determining the shape
x = dtu_f64.shape
print("Image Shape: ")
print(x)
print("\n")

# Extracting pixel from data set
px_d=[] #Temporarily store the pixel after grabbing the pixel at a locaton
px_v=[] # Warehousing the pixels

print("Extracting pixels..\n")

for i in range(dtu_f64.shape[0]):
    for j in range(dtu_f64.shape[1]):
      
      
        for k in dtu_f64[i, j,:]:
           
            px_d.append(k)
           
        px_v.append(px_d) #Storing the the pixel 
        px_d=[] #Empties the pixel to grab a new one
        
# Turning the data into an array
vArray=np.array(px_v)

# Turning the araray into feature vector

vArrayDF=pd.DataFrame(vArray, columns=['r', 'g', 'b'])

# K means Clustering 

print("K means clustering...\n")

km=cluster.KMeans(init='k-means++', n_clusters=64, n_init=10)
km.fit(vArrayDF)
ym=km.predict(vArrayDF)

#  Generating codebook

print("Generating codebook...\n")

codebook=km.cluster_centers_

# Function to return image

def recreate_image(codebook, labels, y, x):
    #Creating all zero 3 dimension matrix. Information from codebook will be used to generate the pixels
    image = np.zeros((y, x, codebook.shape[1])) 
    label_idx = 0
    for i in range(y):
        for j in range(x):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

print("Recreating image...\n")

image=recreate_image(km.cluster_centers_, ym, dtu_f64.shape[0], dtu_f64.shape[1])


imsave('dtu_compressed.jpg', image)