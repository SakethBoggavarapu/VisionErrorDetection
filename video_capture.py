import cv2
import os

os.makedirs("videos", exist_ok=True)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter("videos/test_video.avi", fourcc, 20.0, (width, height))

print("Recording...")
print("Press Q to stop.")

while True:
    success, frame = camera.read()

    if not success:
        break

    video.write(frame)

    cv2.imshow("Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
video.release()
cv2.destroyAllWindows()

print("Video saved successfully!")