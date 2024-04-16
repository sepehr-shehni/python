import cv2

# خواندن تصویر
img = cv2.imread('E:\\Project\\Python Project\\Image-Processing\\1.jpg')

# نمایش تصویر
cv2.imshow('Image', img)

# صبر تا فشرده شدن کلیدی
cv2.waitKey(0)

# بستن پنجره نمایش تصویر
cv2.destroyAllWindows()
