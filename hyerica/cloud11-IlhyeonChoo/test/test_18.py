import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_18 import find_positive_positions


def test():
    arr = np.array([[0, 1], [-2, 3]])
    result = find_positive_positions(arr)
    assert np.sum(result) == 3

