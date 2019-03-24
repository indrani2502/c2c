import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage as ndimage
 
imageFile = '2d.jpg'
mat = cv2.imread(imageFile)
mat = mat[:,:,0] # get the first channel
rows, cols = mat.shape
xv, yv = np.meshgrid(range(cols), range(rows)[::-1])
 
blurred = ndimage.gaussian_filter(mat, sigma=(10, 10), order=0)
fig = plt.figure(figsize=(16,16))
 
ax = fig.add_subplot(221)
ax.imshow(mat, cmap='gray')
 
ax = fig.add_subplot(222, projection='3d')
ax.elev= 250
ax.plot_surface(xv, yv, mat)
 
ax = fig.add_subplot(223)
ax.imshow(blurred, cmap='gray')
 
ax = fig.add_subplot(224, projection='3d')
ax.elev= 400
ax.plot_surface(xv, yv, blurred)
plt.show()
