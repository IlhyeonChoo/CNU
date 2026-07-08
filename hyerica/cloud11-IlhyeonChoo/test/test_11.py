import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_11 import normalize_image


def test():
    img_array = [[[100, 0, 30],
                 [30, 20, 40],
                 [10, 255, 52]], 
                 [[100, 0, 30],
                 [30, 20, 40],
                 [10, 255, 52]],
                 [[100, 0, 30],
                 [30, 20, 40],
                 [10, 255, 52]]]
    assert np.sum(normalize_image(img_array)) == -14.364705882352942

