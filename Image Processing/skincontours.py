import cv2 
import numpy as np 
img=cv2.imread('yo.jpg')
lower=np.array([0,48,80],dtype = "uint8")
upper=np.array([20,255,255], dtype = "uint8")
converted = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
skinMask =cv2.inRange(converted,lower,upper)
contours, hierarchy = cv2.findContours(skinMask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 900,600) 
cv2.imshow("image",img)
cv2.imwrite('detection_contours.jpg',img)
cv2.waitKey()