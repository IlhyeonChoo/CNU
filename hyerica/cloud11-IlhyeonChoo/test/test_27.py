import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_27 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        n, d = np.random.randint(50, 100, size=2)
        X = np.random.randn(n, d)
        target = X.sum(axis=0) / n

        res = solution(X)
        assert np.allclose(res, target, atol=1e-5)

