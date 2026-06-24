import cv2

video_path = "C:/Users/suman/Downloads/15015963-hd_1920_1080_30fps.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open the video file.")
    exit()

frames = []

# Read all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play original video
for frame in frames:
    cv2.imshow("Original Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:  # ESC key
        break

# Play reverse video
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == 27:  # ESC key
        break

cv2.destroyAllWindows()
