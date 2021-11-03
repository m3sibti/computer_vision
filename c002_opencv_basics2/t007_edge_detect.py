from cv2 import cv2
import argparse
import imutils
import numpy as np


def auto_canny(image, sigma=0.33):
    v = np.median(image)

    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, upper)


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
cv2.imshow('org', img)
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Parameters for heresies threshing
wide = cv2.Canny(blur, 10, 200)
mid = cv2.Canny(blur, 30, 150)
tight = cv2.Canny(blur, 240, 250)
auto = auto_canny(blur)

cv2.imshow('wide', wide)
cv2.imshow('mid', mid)
cv2.imshow('tight', tight)
cv2.imshow('auto', auto)

cv2.waitKey(0)
