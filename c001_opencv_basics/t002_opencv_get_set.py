from cv2 import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', type=str, default='./data/tony_stark.jpeg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
(h, w) = img.shape[:2]
print(f'Height: {h}')
print(f'Width: {w}')

# cv2 represents BGR
# x=25 y=10 (rows x cols)
(x, y, z) = img[10, 25]
print(f'Values of R:{z}, G{y}, B{x}')

cv2.imshow('A', img)

cX, cY = (w // 2, h // 2)
# startY:endY, startX:endX
tr = img[0:cY, cX:w]
tl = img[0:cY, 0:cX]
br = img[cY:h, cX:w]
bl = img[cY:h, 0:cX]

# display results
cv2.imshow('TR', tr)
cv2.imshow('BR', br)
cv2.imshow('TL', tl)
cv2.imshow('BL', bl)

img[0:cY, 0:cX] = (0, 0, 255)
cv2.imshow('Updated', img)

cv2.waitKey(0)
