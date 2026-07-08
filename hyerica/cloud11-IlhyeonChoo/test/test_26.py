import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_26 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        d = np.random.randint(2, 100)
        v1, v2 = np.random.randn(2, d)

        target = sum([(e1 - e2)**2 for e1, e2 in zip(v1, v2)]) ** 0.5
        dist = solution(v1, v2)
        assert abs(target - dist) < 1e-5

