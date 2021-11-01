from cv2 import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
cv2.imshow('org', img)
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

"""
Convolution operation just have 3 steps
    1. Take an image and kernel
    2. Perform element-wise multiplication
    3. Sum over all the values
    
An important thing to note is the padding of the image to
keep the edge related information -- PyImageSearch has custom
CONVOLUTION operation code.
"""

ks = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
], dtype='int8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out = cv2.filter2D(gray, -1, ks)
cv2.imshow('res', out)
cv2.waitKey(0)
