from scipy.ndimage import measurements,morphology
from PIL import Image
from numpy import *
from pylab import *
# load image and threshold to make sure it is binary
im = array(Image.open('opencv.jpeg').convert('L'))
im = 1*(im<128)
im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)
labels_open, nbr_objects_open = measurements.label(im_open)

figure()
gray()
subplot(2,4,1)
imshow(im)

subplot(2,4,2)
imshow(labels_open)

plot(measurements.center_of_mass(im_open,labels_open),r*)
show()
