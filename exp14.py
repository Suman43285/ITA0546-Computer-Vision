import cv2
import numpy as np
if __name__ == '__main__':
    im_src = cv2.imread("C:/personal/computer vision/images/8.jpeg")
    if im_src is None:
        print("Source image not found!")
        exit()
    pts_src = np.array([
        [141, 131],
        [480, 159],
        [493, 630],
        [64, 601]
    ], dtype=float)
    im_dst = np.zeros((800, 800, 3), dtype=np.uint8)
    pts_dst = np.array([
        [318, 256],
        [534, 372],
        [316, 670],
        [73, 473]
    ], dtype=float)
    h, status = cv2.findHomography(pts_src, pts_dst)
    im_out = cv2.warpPerspective(
        im_src,
        h,
        (im_dst.shape[1], im_dst.shape[0])
    )
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Canvas", im_dst)
    cv2.imshow("Warped Source Image", im_out)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
