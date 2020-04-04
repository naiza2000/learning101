import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('robot.jpg')
img =cv2.resize(img,(1152,864))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template = cv2.imread('t1.jpg',0)
template = cv2.resize(template,(220,132))
w, h = template.shape[::-1]

    # Apply template Matching
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
loc = np.where(res >= threshold) 

#top_left = min_loc
    
#bottom_right = (top_left[0] + w, top_left[1] + h)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h), (0,255,255), 2)
cv2.imshow('final',img)
cv2.waitKey()
