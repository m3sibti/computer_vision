import numpy as np
from cv2 import cv2
import os


class SimpleDatasetLoader:

    def __init__(self, preprocessors=None):
        self.preprocessors = preprocessors

        if preprocessors is None:
            self.preprocessors = []

    def load(self, img_paths, verbose=-1):
        data = []
        labels = []

        for (i, img_path) in enumerate(img_paths):
            img = cv2.imread(img_path)
            label = img_path.split(os.path.sep)[-2]

            if (preprocessors := self.preprocessors) is not None:
                for p in preprocessors:
                    img = p.preprocess(img)

            data.append(img)
            labels.append(label)

            if verbose > 0 and i > 0 and (i + 1) % verbose == 0:
                print(f'[INFO] processed {i + 1}/{len(img_paths)}')

        return np.array(data), np.array(labels)
