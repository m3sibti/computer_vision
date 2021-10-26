from cv2 import cv2
import argparse
import numpy as np

# ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--input_image', type=str, default='./data/tony_stark.jpeg')
# vars(argparse)

canvas = np.zeros((300, 300), dtype='uint8')
cv2.imshow('Image', canvas)
cv2.waitKey(0)

cv2.line(canvas, (0, 0), (300, 300), (0, 255, 0), 1)
cv2.imshow('Image', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (120, 120), (180, 180), (0, 255, 0), -1)
cv2.imshow('Image', canvas)
cv2.waitKey(0)

for i in (0, 175, 25):
    cv2.circle(canvas, (25, 26), i, (255, 255, 255), 1)
    cv2.imshow('Image', canvas)

cv2.waitKey(0)

# getting random ranges
color = np.random.randint(0, high=256, size=(3,)).tolist()
pt = tuple(np.random.randint(0, high=600, size=(2,)))
cv2.circle(canvas, pt, 25, (0, 255, 0), 2)
cv2.waitKey(0)
