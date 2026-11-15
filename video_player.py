# This is a new file that will be used to play the video in a separate window, 
# so that the main program can continue running without being blocked by the video playback.
import cv2


def play_video(filename="Video.mp4"):
    video = cv2.VideoCapture(filename)

    if not video.isOpened():
        print(f"Could not open {filename}")
        return

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    delay = max(1, int(1000 / fps)) if fps > 0 else 33

    print("Video loaded successfully!")
    print("FPS:", fps)
    print("Total frames:", frame_count)

    try:
        while True:
            success, frame = video.read()

            if not success:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            cv2.imshow("KickVision", frame)

            if cv2.waitKey(delay) & 0xFF == ord("q"):
                break
    finally:
        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    play_video()
