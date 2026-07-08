import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_06 import solution


def test_solution():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "color.png")).convert("RGB")
    image = np.array(image)

    r, g, b = solution(image)
    assert np.all(np.abs(np.stack([r, g, b], axis=-1) - image) < 1e-4)
