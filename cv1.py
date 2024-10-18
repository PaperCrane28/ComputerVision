import cv2
import numpy as np
import pytesseract
from pytesseract import Output

img = cv2.imread('1.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

image = cv2.imread('1.jpg')

gray = get_grayscale(image)
thresh = thresholding(gray)
opening = opening(gray)
deskew = deskew(gray)
canny = canny(gray)
erode = erode(gray)

img = gray
cv2.imshow('gray', img)
# Adding custom options
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

img = thresh
cv2.imshow('thresh', img)
# Adding custom options
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

img = opening
cv2.imshow('opening', img)
# Adding custom options
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

img = canny
cv2.imshow('canny', img)
# Adding custom options
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

img = deskew
cv2.imshow('deskew', img)
# Adding custom options
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

img = erode
cv2.imshow('erode', img)
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)


cv2.waitKey(0)
cv2.destroyAllWindows()

img = image
cv2.imshow('origin', img)
# Adding custom options
custom_config = r'--oem 1 --psm 6'
pytesseract.image_to_string(img, config=custom_config)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

img = cv2.imread('origin', img)

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)

cv2.imshow('box', img)

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 50:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv2.imshow('boxes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

