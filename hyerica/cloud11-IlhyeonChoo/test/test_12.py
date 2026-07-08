import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_12 import mean_of_filtered_pixels


def test():
    img_array = [[120, 135], 
                 [200, 90]]
    result = mean_of_filtered_pixels(img_array)
    assert result == 167.5

