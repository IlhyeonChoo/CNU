import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_19 import count_pixels_over_threshold


def test():
    img_array = np.array([
        [100, 120, 180, 200],
        [210, 250, 90, 80],
        [130, 70, 60, 255]
    ])
    result = count_pixels_over_threshold(img_array, 180)
    assert result == 4

