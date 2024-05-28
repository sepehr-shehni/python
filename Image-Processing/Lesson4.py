import cv2
import numpy as np

def draw_shapes(frame):
    # Draw a line
    cv2.line(frame, (100, 200), (200, 400), (10, 30, 130), 20)
    
    # Draw a rectangle
    cv2.rectangle(frame, (100, 200), (200, 300), (0, 0, 255), 5)
    
    # Draw a circle
    cv2.circle(frame, (400, 200), 70, (120, 0, 50), 3)
    
    # Draw a polygon
    pts = np.array([[50, 100], [120, 200], [250, 100], [400, 20]])
    cv2.polylines(frame, [pts], True, (60, 40, 20), 5)
    
    # Add text
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, 'sepehr shehni', (50, 50), font, 1, (100, 20, 255), 2)

def main():
    cap = cv2.VideoCapture(1)
    
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame")
            break
        
        # Draw shapes on the frame
        draw_shapes(frame)
        
        cv2.imshow('webcam', frame)
        
        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
