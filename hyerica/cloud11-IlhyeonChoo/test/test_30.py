import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_30 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        n = np.random.randint(100, 200)
        X = np.random.randn(n, 2)
        mean = np.random.randn(2, 2)
        mean[0] * 10
        std = np.random.rand(2, 2) + 0.1

        res = solution(X, mean, std)
        assert np.allclose(res[:n//2].mean(axis=0), mean[0], atol=1e-4) and np.allclose(res[n//2:].mean(axis=0), mean[1], atol=1e-4) \
            and np.allclose(res[:n//2].std(axis=0), std[0], atol=1e-4) and np.allclose(res[n//2:].std(axis=0), std[1], atol=1e-4)
