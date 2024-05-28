import cv2

# Open webcam
cap = cv2.VideoCapture(1)

# Check if webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# Define codec and create VideoWriter object
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', codec, 24.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Check if frame is captured successfully
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Convert frame to grayscale
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the frame to the output video
    out.write(frame)

    # Display the frame
    cv2.imshow('webcam', color)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
