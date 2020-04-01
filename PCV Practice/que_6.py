from scipy.ndimage import measurements,morphology
from numpy import *
from pylab import *
from PIL import Image
# load image and threshold to make sure it is binary
im = array(Image.open('opencv.jpeg').convert('L'))
im = 1*(im<120)
labels, nbr_objects = measurements.label(im)
imshow(im)
figure()
hist(im.flatten(),120)
show()