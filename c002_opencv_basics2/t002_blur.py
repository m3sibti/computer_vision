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


def get_blurred_func(f_name=''):
    if f_name.lower() == 'blur':
        return cv2.blur  # simple blurring
    elif f_name.lower() == 'gaussian':
        return cv2.GaussianBlur  # natural effect
    elif f_name.lower() == 'median':
        return cv2.medianBlur  # for slat and pepper
    return cv2.blur


# mostly odd sizes, because of center concept
kernel_sizes = [(3, 3), (9, 9), (15, 15)]
for (kX, kY) in kernel_sizes:
    blurred_img = get_blurred_func('blur')(img, (kX, kY))
    cv2.imshow(f'res_{kX}', blurred_img)
    cv2.waitKey(0)

# bilateral
bilateral_filter_list = [(11, 21, 7), (11, 43, 13), (11, 69, 19)]
for (d, sigmaColor, sigmaSpace) in bilateral_filter_list:
    blurred_img = cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace, )
    cv2.imshow(f'res_{d}_{sigmaColor}_{sigmaSpace}', blurred_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
