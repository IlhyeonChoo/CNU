import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_13 import adjust_brightness


def test():
    img_array = [[[100, 150, 180, 210, 255],
                 [90, 120, 200, 220, 250],
                 [80, 110, 190, 230, 240],
                 [70, 130, 160, 240, 245],
                 [60, 140, 170, 250, 255]],
                [[200, 190, 180, 170, 160],
                 [150, 140, 130, 120, 110],
                 [100,  90,  80,  70,  60],
                 [ 50,  40,  30,  20,  10],
                 [  0,  25,  50,  75, 100]],
                [[ 10,  20,  30,  40,  50],
                 [ 60,  70,  80,  90, 100],
                 [110, 120, 130, 140, 150],
                 [160, 170, 180, 190, 200],
                 [210, 220, 230, 240, 250]]]
    result = adjust_brightness(img_array)
    assert result == 8247.5

