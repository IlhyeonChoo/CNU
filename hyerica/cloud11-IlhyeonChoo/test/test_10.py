import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_10 import solution


def test_solution():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    image = Image.open(os.path.join(root_dir, "resources", "data", "test_image.jpg")).convert("L")
    image = np.array(image)

    H, W = image.shape

    for _ in range(10):
        mask = np.random.randint(0, 2, size=(H, W))
        mask[mask == 1] = 255
        mask = mask.astype(np.uint8)
        
        image_cp = image + 0
        masked_image = solution(image_cp, mask)
        masked_image = masked_image.astype(np.int32) - (255 - mask.astype(np.int32))
        
        assert (masked_image == -255).astype(np.int32).sum() == (mask == 0).astype(np.int32).sum()

