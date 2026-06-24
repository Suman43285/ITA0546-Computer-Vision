import cv2
image=cv2.imread("C:/personal/computer vision/images/butterfly.jpeg")
edges=cv2.Canny(image,threshold1=30,threshold2=100)
cv2.imshow('original image',image)
cv2.imshow('canny image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
