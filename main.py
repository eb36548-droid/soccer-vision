import cv2

video = cv2.VideoCapture("video.mp4")

if not video.isOpened():
    print("Could not open video.mp4")
else:
    success, frame = video.read()

    if success:
        print("Video loaded successfully!")
        print("Frame dimensions:", frame.shape[1], "x", frame.shape[0])
    else:
        print("Video opened, but no frame could be read.")

video.release()