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

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# There are multiple ways of calculating histograms
#    - GrayScale | RGB | Single Channel | 2D | 3D
#    - Histograms can also be taken with masks
hist = cv2.calcHist(gray, [0], None, [256], [0, 256])

# show plot of histograms

# --- Adaptive Histograms ---
#      SIMPLE & CLAHE

# cv2.equalizeHist()
# cv2.createClahe() then apply that clahe

# Histogram Matching (for consistence lighting conditions)
# 1 - Color Transfer without Machine Learning
# 2 - skimage import exposure
