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

# resize by keeping the aspect ratio
r = (150 / w)
dim = (150, int(h * r))
out = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('res1', out)

res2 = imutils.resize(img, width=150)
cv2.imshow('res2', res2)
cv2.waitKey(0)
# using the utils functions
methods = [
    # if going to downscale
    ('cv2.INTER_LINEAR', cv2.INTER_LINEAR),
    ('cv2.INTER_AREA', cv2.INTER_AREA),
    ('cv2.INTER_NEAREST', cv2.INTER_NEAREST),
    # if going to do up-scale
    ('cv2.INTER_CUBIC', cv2.INTER_CUBIC),
    ('cv2.INTER_LANCZOS4', cv2.INTER_LANCZOS4),
]
