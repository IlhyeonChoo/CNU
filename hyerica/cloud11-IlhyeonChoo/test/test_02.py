import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np

from question_02 import solution


def test_solution():
    np.random.seed(18)

    for _ in range(10):
        x_start = np.random.randint(0, 100)
        x_end = np.random.randint(x_start + 10, x_start + 100)
        x = np.arange(x_start, x_end)

        gradient = np.random.randint(-10, 10)
        gradient = gradient + 1 if gradient == 0 else gradient

        y_int = np.random.randint(-10, 10)

        y = solution(x, gradient, y_int)
        y_gt = x*gradient + y_int

        assert abs((y - y_gt).mean()) < 1e-4


