from cv2 import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

# codes for flipping
#    .  1: Horizontal
#    .  0: Vertical
#    . -1: Both
hor_flip = cv2.flip(img, 1)
cv2.imshow('res', hor_flip)
cv2.waitKey(0)
