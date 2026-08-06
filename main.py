import cv2

# Open the default webcam
camera = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started successfully!")
print("Press 'q' to quit.")

while True:
    # Capture one frame
    success, frame = camera.read()

    if not success:
        print("Failed to capture frame.")
        break

    # Show the live video
    cv2.imshow("Live Webcam Feed", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
camera.release()
cv2.destroyAllWindows()