import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_15 import mean_subtract_channels


def test():
    img_array = np.array([[[100, 150, 200], [50, 50, 50]],
                          [[150, 200, 100], [200, 100, 0]]], dtype=np.uint8)

    result = mean_subtract_channels(img_array)
    assert np.sum(result) == 0.0

