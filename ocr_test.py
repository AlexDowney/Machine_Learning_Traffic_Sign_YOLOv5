import cv2
from PIL import Image
import pytesseract
import numpy as np
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

FILEPATH = './test6.jpg' # "./yolov5/runs/detect/exp5/crops/mandatory/00214.jpg"

FILEPATH = "./yolov5/runs/detect/exp5/crops/other/00214.jpg"

image_obj = Image.open(FILEPATH)

img = cv2.imread(FILEPATH)

cv2.imshow("img", img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#threshold the image
_, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# get horizontal mask of large size since text are horizontal components
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

# find all the contours
contours, hierarchy,=cv2.findContours(connected.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#Segment the text lines
counter=0
array_of_texts=[]
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    cropped_image = image_obj.crop((x-10, y, x+w+10, y+h ))
    str_store = re.sub(r'([^\s\w]|_)+', '', pytesseract.image_to_string(cropped_image))
    array_of_texts.append(str_store)
    counter+=1

print(array_of_texts)




"""
cv2.imshow('original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()
#Create MSER object
mser = cv2.MSER_create()
#detect regions in gray scale image
regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)
mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
for contour in hulls:
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
text_only = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("text only", text_only)
cv2.waitKey(0)
"""

"""
sharpen_filter = np.array([[-1,-1,-1],
                            [-1, 9,-1],
                            [-1,-1,-1]])

sharp_img = cv2.filter2D(img, -1, sharpen_filter)
sharper_img = cv2.filter2D(sharp_img, -1, sharpen_filter)

cv2.imshow("img", img)
cv2.imshow("sharp_img", sharp_img)
cv2.imshow("sharper_img", sharper_img)


# Simple image to string
print(pytesseract.image_to_string(img), 'xxx')
print(pytesseract.image_to_string(sharp_img), 'xxx')
print(pytesseract.image_to_string(sharper_img), 'xxx')
"""


cv2.waitKey(0)
cv2.destroyAllWindows()
