from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
im = array(Image.open('obj.jpg').convert('L'))
#Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)
imy = zeros(im.shape)
filters.sobel(im,0,imy)
magnitude = sqrt(imx**2+imy**2)
imshow(magnitude)
show()