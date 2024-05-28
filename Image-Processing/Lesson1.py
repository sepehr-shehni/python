import cv2
import os

def display_image(image_path):
    """Read and display an image using OpenCV."""
    try:
        # Read the image
        img = cv2.imread(image_path)

        if img is None:
            print("Error: Unable to load the image.")
            return

        # Display the image
        cv2.imshow('Image', img)

        # Wait for a key press and then close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("An error occurred:", e)

def main():
    """Main function."""
    # Define the image file path
    image_path = os.path.join('E:\\python project\\Image-Processing\\1.jpg')

    # Display the image
    display_image(image_path)

if __name__ == "__main__":
    main()
