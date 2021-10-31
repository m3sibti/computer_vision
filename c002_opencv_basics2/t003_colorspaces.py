from cv2 import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
cv2.imshow('org', img)
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb_img)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv_img)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow('lab', lab_img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_img)

cv2.waitKey(0)

cv2.destroyAllWindows()
