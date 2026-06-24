import cv2
import numpy as np

img1 = cv2.imread("C:/personal/computer vision/images/2.jpeg")
img2 = cv2.imread("C:/personal/computer vision/images/9.jpeg")

if img1 is None:
    print("Error loading img1")
    exit()

if img2 is None:
    print("Error loading img2")
    exit()

pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[100, 100], [300, 100], [100, 300], [300, 300]])

H, status = cv2.findHomography(pts1, pts2)

dst = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
