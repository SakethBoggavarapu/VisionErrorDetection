import cv2
import os

# Create the images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started successfully!")
print("Press 'S' to save an image.")
print("Press 'Q' to quit.")

image_count = 1

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to capture frame.")
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"images/image_{image_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        image_count += 1

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
