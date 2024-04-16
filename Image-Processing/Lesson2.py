import cv2

# خواندن تصویر
img = cv2.imread('E:\\Project\\Python Project\\Image-Processing\\1.jpg')

# تبدیل تصویر به سیاه و سفید
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# نمایش تصویر سیاه و سفید
cv2.imshow('Grayscale Image', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
