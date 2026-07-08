import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_09 import solution


def test_solution():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("L")
    image = np.array(image)

    H, W = image.shape

    for _ in range(10):
        x1 = np.random.randint(0, W//2)
        y1 = np.random.randint(0, H//2)
        x2 = np.random.randint(x1 + 10, W)
        y2 = np.random.randint(y1 + 10, H)
        mask = solution(image, x1, y1, x2, y2)

        mask = mask.astype(np.float32) / 255
        assert abs(mask.sum() - (y2 - y1)*(x2 - x1)) < 1e-4
