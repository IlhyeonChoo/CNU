import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_25 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        A = np.random.randn(10, 10)
        A = A.reshape(-1)
        target = np.array([2.71828 ** a / (1 + 2.71828 ** a) for a in A])

        B = solution(A)
        B = B.reshape(-1)

        assert np.allclose(B, target, atol=1e-5)
