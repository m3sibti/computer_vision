from cv2 import cv2


class SimplePreProcessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, img):
        """
        Resize the image, ignore the aspect ratio
        :param img:
        :return:
        """
        return cv2.resize(img, (self.width, self.height), interpolation=self.inter)
