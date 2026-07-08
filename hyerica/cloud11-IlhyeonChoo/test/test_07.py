import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_07 import solution


def test_solution():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("RGB")
    image = np.array(image)

    H, W, _ = image.shape

    for _ in range(10):
        x1 = np.random.randint(0, W//2)
        y1 = np.random.randint(0, H//2)
        x2 = np.random.randint(x1 + 10, W)
        y2 = np.random.randint(y1 + 10, H)
        cropped = solution(image, x1, y1, x2, y2)
        kH, kW, _ = cropped.shape
        assert kH == y2 - y1 and kW == x2 - x1
        _matching(image, cropped, x1, y1)


def _matching(image, cropped, x1, y1):
    H, W, _ = image.shape
    kH, kW, _ = cropped.shape

    ret = (image[y1:y1+kH, x1:x1+kW] * cropped).sum()
    assert abs(ret - (cropped*cropped).sum()) < 1e-4




