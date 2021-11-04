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

# Adjust the lighting
# lower gamma values leads to darker images
# higher gamma values leads to lighter (more visible) images
# O=I ^ (1/G) -- create a table (np_array) and use cv2.LUT()
