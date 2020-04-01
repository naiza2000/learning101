from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
im = array(Image.open('opencv.jpeg').convert('L'))
im1 = filters.gaussian_filter(im,6)
im1=uint8(im1)
im2=im1-im
im3=im-im2
imshow(im3)
figure()
im4 = array(Image.open('opencv.jpeg'))
im5 = zeros(im4.shape)
for i in range(3):
    im5[:,:,i] = filters.gaussian_filter(im4[:,:,i],6)
im5 = uint8(im5)
im6=im5-im4
im7=im4-im6
imshow(im7)
show()