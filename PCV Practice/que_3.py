from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('opencv.jpeg'))
im1 = zeros(im.shape)
for i in range(3):
    im1[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
im1 = uint8(im1)
im2 = im/im1
imshow(im2)
show()