from cv2 import cv2
import argparse
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

# get rotation matrix and rotate + (counter-clock) - (clock-wise)
M = cv2.getRotationMatrix2D((cX, cY), 45, 1)
rt_cv = cv2.warpAffine(img, M, (w, h))
cv2.imshow('res1', rt_cv)

# rotate using imutils
rt = imutils.rotate(img, 45)
cv2.imshow('res2', rt)

# rotate by keeping in view the translation
rt_bound = imutils.rotate_bound(img, 45)
cv2.imshow('res3', rt_bound)

cv2.waitKey(0)
