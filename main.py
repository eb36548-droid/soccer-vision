
import cv2

# this should be a test to see if the video can be loaded and played back correctly
video = cv2.VideoCapture("Video.mp4")

if not video.isOpened():
    print("Could not open Video.mp4")
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    print("Video loaded successfully!")
    print("FPS:", fps)
    print("Total frames:", frame_count)

    # this is the delay between frames in milliseconds, calculated based on the FPS of the video
    delay = max(1, int(1000 / fps)) if fps > 0 else 33

    while True:
        success, frame = video.read()

        if not success:
            break

        # Displays the current video frame
        cv2.imshow("SoccerVision - Video Test", frame)

        # disable keybinds to allow me to exit the video playback early with the "q" key
        if cv2.waitKey(delay) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()
    print("Video playback finished.")
