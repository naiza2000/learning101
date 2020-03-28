import cv2 
import numpy as np 
img=cv2.imread('yo.jpg')
lower=np.array([0,48,80],dtype = "uint8")
upper=np.array([20,255,255], dtype = "uint8")
converted = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
skinMask =cv2.inRange(converted,lower,upper)
cv2.imwrite('detection.png',skinMask)
cv2.imshow("images",skinMask)
cv2.waitKey()