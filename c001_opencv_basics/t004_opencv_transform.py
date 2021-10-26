from cv2 import cv2
import argparse
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_image', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_image'])
matrix = np.float32([[1., 0., 0.], [0., 1., 150.]])
print(matrix.shape)
res = cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))
cv2.imshow('res1', res)
res2 = imutils.translate(img, 0, 150)
cv2.imshow('res2', res2)
cv2.waitKey(0)
