import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_08 import solution


def test_solution():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("RGB")
    image = np.array(image)

    H, W, _ = image.shape

    for _ in range(10):
        image_cp = image + 0
        x1 = np.random.randint(0, W//2)
        y1 = np.random.randint(0, H//2)
        x2 = np.random.randint(x1 + 10, W)
        y2 = np.random.randint(y1 + 10, H)
        image_cp = solution(image_cp, x1, y1, x2, y2)

        assert np.all(np.abs(image[:y1] - image_cp[:y1]) < 1e-4)
        assert np.all(np.abs(image[y2:] - image_cp[y2:]) < 1e-4)
        assert np.all(np.abs(image[:, :x1] - image_cp[:, :x1]) < 1e-4)
        assert np.all(np.abs(image[:, x2:] - image_cp[:, x2:]) < 1e-4)
        assert np.sum(image_cp[y1:y2, x1:x2]) < 1e-4
