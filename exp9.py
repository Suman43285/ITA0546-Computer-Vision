import cv2

def play_video(video_path, speed=1.0, window_name="Video"):
    cap = cv2.VideoCapture("C:/Users/suman/Downloads/15015963-hd_1920_1080_30fps.mp4")

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    while True:
        ret, frame1 = cap.read()
        ret2, frame2 = cap.read()

        if not ret or not ret2:
            break

        cv2.imshow("Original Video", frame1)
        cv2.imshow("Slow Video", frame2)

        delay = int(1000 / (fps * speed))

        if cv2.waitKey(delay) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

play_video("C:/Users/suman/Downloads/whats.mp4")
play_video("C:/Users/suman/Downloads/whats.mp4", speed=0.1)
