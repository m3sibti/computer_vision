from cv2 import cv2
import argparse
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

# cv2 clip and numpy wrap around-items to stop


# OpenCV keep the value range around (0, 255) by clipping
M = np.ones(img.shape, dtype='uint8') * 100
res_add = cv2.add(img, M)
cv2.imshow('Lighter', res_add)

# OpenCV keep the value range around (0, 255) by clipping
M = np.ones(img.shape, dtype='uint8') * 50
res_sub = cv2.subtract(img, M)
cv2.imshow('Darker', res_sub)

cv2.waitKey(0)
