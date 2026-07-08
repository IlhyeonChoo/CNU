import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_16 import set_positions


def test():
    result = set_positions((3, 3), [(0, 1), (2, 2)], 9)
    assert np.sum(result) == 18

