
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera")
    exit()

file_name = input("Enter video file name (e.g. video.avi): ")

recorder = None
is_recording = False

print("Press 1 to start recording")
print("Press 2 to stop and save the video")
print("Press Q to exit")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read frame")
        break

    if is_recording:
        cv2.putText(
            frame,
            "REC",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )
        recorder.write(frame)

    cv2.imshow("PyCam Video Recorder", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1') and not is_recording:
        height, width = frame.shape[:2]
        codec = cv2.VideoWriter_fourcc(*"XVID")

        recorder = cv2.VideoWriter(
            file_name,
            codec,
            20.0,
            (width, height)
        )

        if recorder.isOpened():
            is_recording = True
            print("Recording started")
        else:
            print("Could not create video file")
            recorder.release()
            recorder = None

    elif key == ord('2') and is_recording:
        recorder.release()
        recorder = None
        is_recording = False
        print(f"Video saved as {file_name}")

    elif key == ord('q'):
        break

if recorder is not None:
    recorder.release()

camera.release()
cv2.destroyAllWindows()
