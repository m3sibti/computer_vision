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

# split opencv chanels
[B, G, R] = cv2.split(img)
cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.waitKey(0)

# merge them back
merged = cv2.merge([B, G, R])
cv2.imshow('merged', merged)
cv2.waitKey(0)

zeros = np.zeros(G.shape, dtype='uint8')
cv2.imshow('B-Only', cv2.merge([B, zeros, zeros]))
cv2.imshow('G-Only', cv2.merge([zeros, G, zeros]))
cv2.imshow('R-Only', cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
