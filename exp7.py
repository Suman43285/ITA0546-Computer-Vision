import cv2
import numpy as np
image=cv2.imread("C:/personal/computer vision/images/strawberry.jpeg")
kernel=np.ones((5,5),np.uint8)
dilated_image=cv2.dilate(image,kernel,iterations=1)
cv2.imshow('original image',image)
cv2.imshow('dilated image',dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
