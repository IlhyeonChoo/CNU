import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_29 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        d = np.random.randint(2, 100)
        v1, v2 = np.random.randn(2, d)

        target = np.cov(v1[None], v2[None])[0, 1]
        cov = solution(v1, v2)
        assert abs(target - cov) < 1e-5
