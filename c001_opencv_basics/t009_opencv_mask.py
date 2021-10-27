from cv2 import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
cv2.imshow('org', img)
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

mask = np.zeros(img.shape[:2], dtype='uint8')
cv2.rectangle(mask, (cX, cY), (cX + 300, cY + 300), (255, 255, 255), -1)
cv2.imshow('mask', mask)

res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('res', res)

cv2.waitKey(0)
