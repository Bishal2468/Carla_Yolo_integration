# utils/helpers.py

import numpy as np
import cv2

def process_image(image):
    return np.reshape(np.copy(image.raw_data), (image.height, image.width, 4))