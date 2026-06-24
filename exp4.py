import cv2
image=cv2.imread("C:/personal/computer vision/images/butterfly.jpeg")
cv2.imshow('original',image)
cv2.waitKey(0)
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated image',rotated)
cv2.WaitKey(0)
cv2.destroyAllWindows()
