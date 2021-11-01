from cv2 import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', default='./data/m_pic.jpg')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
(h, w) = img.shape[:2]
cX, cY = w // 2, h // 2

"""
Image Gradients are classical computer vision technique
    - It perform convolution operation
    - Detect North, South, West, East pixels
    - Perform North-South and West-East to detect changes in Y and X direction
      & Magnitude of change
    - Use ArcTangent to find the angle of changes
"""

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('org', gray)

# for Sobel use 3 else -1
gX = cv2.Sobel(gray, cv2.CV_32F, dx=1, dy=0, ksize=3)
gY = cv2.Sobel(gray, cv2.CV_32F, dx=0, dy=1, ksize=3)
cv2.imshow('gX', gX)
cv2.imshow('gY', gY)

# convert back to uint8
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine using addWeighted
out = cv2.addWeighted(gX, 0.5, gY, 0.5, 0.0)
cv2.imshow('out', out)

cv2.waitKey(0)
cv2.destroyAllWindows()
