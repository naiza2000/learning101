from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
im = array(Image.open('opencv.jpeg').convert('L'))
for i in range(1,5):
    im2 = filters.gaussian_filter(im,2*i)
    gray()
    axis('off')
    imshow(im2)
    figure()
    contour(im2, origin='image')
    axis('off')
    show()


#contours are becoming less distinct as the image gets more and more blurred.    
    
