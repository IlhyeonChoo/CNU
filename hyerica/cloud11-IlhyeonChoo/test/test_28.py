import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_28 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        n, d = np.random.randint(50, 100, size=2)
        X = np.random.randn(n, d).astype(np.float64)
        target1 = X.sum(axis=0) / n
        target2 = (np.sum((X - target1)**2, axis=0) / (n - 1)) ** 0.5
        target3 = (np.sum((X - target1)**2, axis=0) / n) ** 0.5
        target4 = (X - target1) / target2
        target5 = (X - target1) / target3

        res = solution(X)

        assert np.allclose(res, target4, atol=1e-5) or np.allclose(res, target5, atol=1e-5)

