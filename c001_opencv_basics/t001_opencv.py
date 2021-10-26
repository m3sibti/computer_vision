import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input_img', required=True, help='Path to the input image')
ap.add_argument('-o', '--output_img', required=True, help='Path to the output image')
args = vars(ap.parse_args())

img = cv2.imread(args['input_img'])
(h, w, c) = img.shape[:3]

print(f'Height: {h}')
print(f'Width: {w}')
print(f'Channels: {c}')

cv2.imshow('Window', img)
cv2.waitKey(0)
# cv2.imwrite(args['output_img'], img)
