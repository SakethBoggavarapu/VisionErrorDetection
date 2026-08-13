import cv2
import os
from datetime import datetime


def start_camera():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Webcam started successfully!")
    print("Press 'S' to save an image.")
    print("Press 'Q' to quit.")

    os.makedirs("saved-images", exist_ok=True)

    # Create a unique timestamp folder
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_path = os.path.join("saved-images", timestamp)
    os.makedirs(folder_path, exist_ok=True)

    # Image counter
    image_count = 1

    while True:
        success, frame = camera.read()

        if not success:
            print("Failed to capture frame.")
            break

        cv2.imshow("Webcam", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            save_image(frame, folder_path, image_count)
            image_count += 1

        elif key == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def save_image(frame, folder_path, image_count):

    # Save the image with a unique number
    image_path = os.path.join(folder_path, f"image_{image_count}.jpg")
    cv2.imwrite(image_path, frame)

    print(f"Image saved: {image_path}")


start_camera()