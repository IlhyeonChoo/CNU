import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_17 import absolute_difference


def test():
    a = np.array([5, 1, 9])
    b = np.array([2, 4, 3])
    result = absolute_difference(a, b)
    assert np.sum(result) == 12

