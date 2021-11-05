from cv2 import cv2
import argparse
import imutils
from skimage.exposure import is_low_contrast

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
cv2.imshow('org', img)
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if is_low_contrast(gray, 0.3):
    print('Low Contrast')
else:
    cv2.imshow('show', gray)
    cv2.waitKey(0)
