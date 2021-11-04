from cv2 import cv2
import argparse
from skimage import exposure

ap = argparse.ArgumentParser()
ap.add_argument('-s', '--source_img', default='./data/tony_stark.jpeg')
ap.add_argument('-r', '--ref_img', default='./data/m_pic.jpg')
args = vars(ap.parse_args())

src_img = cv2.imread(args['source_img'])
ref_img = cv2.imread(args['ref_img'])
cv2.imshow('src_img', src_img)
cv2.imshow('ref_img', ref_img)

multi_channel = True if src_img.shape[-1] > 1 else False
matched = exposure.match_histograms(src_img, ref_img, multichannel=multi_channel)
cv2.imshow('matched', matched)

cv2.waitKey(0)
