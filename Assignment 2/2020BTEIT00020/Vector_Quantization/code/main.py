import os
import matplotlib.pyplot as plt
import python_utils
import numpy as np
# Vector quantization for compressing images
from quantize_image import Quantize

# load image
image_path = os.path.join(os.path.dirname(__file__), 'images', 'icon.png')
img = plt.imread(image_path)
shape = np.shape(img)
print(shape)
img = np.reshape(img,(np.size(img)//4,4))
#print(np.shape(img))
model = Quantize(b=6)
model.quantize(img)
model.dequantize(img)
img = np.reshape(img,shape)
        

        
        #utils.plot_2dclustering(img, model.dequantize(img))
        
fname = os.path.join("..", "figs", "quantize.png")
plt.imsave(fname, img)
        #plt.imshow(img)
        #plt.show
        #plt.savefig(fname)
        
print("\nFigure saved as '%s'" % fname)
