import cv2
import os

def main():
    # Define the path to the image file
    image_path = os.path.join('E:\\python project\\Image-Processing\\1.jpg')

    # Check if the image file exists
    if not os.path.isfile(image_path):
        print("Error: Image file '{}' not found.".format(image_path))
        return

    # Load the image
    img = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if img is None:
        print("Error: Failed to load the image '{}'.".format(image_path))
        return

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_img)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
