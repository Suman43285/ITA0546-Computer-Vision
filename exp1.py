import cv2
image=cv2.imread("C:/personal/computer vision/images/butterfly.jpeg")
cv2.imshow('original',image)
cv2.waitKey(0)
gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_scale',gray_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()
