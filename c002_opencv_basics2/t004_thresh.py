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
# performed blur to ignore the details
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# performed the OTSU threshold that assume the bi-model pixel intensity distribution
# otherwise select the threshold value manually
(T, thresh_inv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow('thresh', thresh_inv)
print(f'Thresh Value: {T}')

# always go for Gaussian C as first option otherwise,
# we have MEAN_C with last param as 10
adap_thresh = cv2.adaptiveThreshold(blurred, 255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV,
                                    21, 4)
cv2.imshow('thresh adaptive', adap_thresh)

# masked = cv2.bitwise_and(img, img, mask=thresh_inv)
# cv2.imshow('res', masked)
cv2.waitKey(0)
