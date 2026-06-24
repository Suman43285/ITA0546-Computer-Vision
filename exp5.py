import cv2
import numpy as np

image = cv2.imread("C:/personal/computer vision/images/9.jpeg")

if image is None:
    print("Image not found!")
    exit()

h, w = image.shape[:2]

canvas_h = 600
canvas_w = 800

x = 50
y = 50

dx = 10
dy = 5

while True:
    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

    # Bounce at boundaries
    if x <= 0 or x + w >= canvas_w:
        dx = -dx

    if y <= 0 or y + h >= canvas_h:
        dy = -dy

    x += dx
    y += dy

    canvas[y:y+h, x:x+w] = image

    # Show original image
    cv2.imshow("Original Image", image)

    # Show moving image
    cv2.imshow("Moving Image", canvas)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
