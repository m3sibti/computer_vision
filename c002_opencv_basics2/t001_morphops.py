from cv2 import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('org', img)
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

kernel_size = (3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
# we have following type of morphological operations
# 1. erode  2. dilate   3. open     4. close
# 5. black-hat  6. top-(white)-hat
res = cv2.morphologyEx(gray.copy(), cv2.MORPH_OPEN, kernel)
cv2.imshow('res', res)
cv2.waitKey(0)
