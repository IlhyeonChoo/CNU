import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_20 import l2_distance


def test():
    points = np.array([[1, 2], [4, 6], [7, 8]])
    query = np.array([1, 1])
    result = l2_distance(points, query)
    assert np.sum(result) == 16.05049635213819

