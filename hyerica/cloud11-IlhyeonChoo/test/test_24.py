import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_24 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        d = np.random.randint(2, 100)
        v1, v2 = np.random.randn(2, d)

        cossim = solution(v1, v2)
        v1_norm = sum([e**2 for e in v1]) ** 0.5
        v2_norm = sum([e**2 for e in v2]) ** 0.5
        target = sum([(e1 / v1_norm) * (e2 / v2_norm) for e1, e2 in zip(v1,  v2)] )
        assert abs(cossim - target) < 1e-5

