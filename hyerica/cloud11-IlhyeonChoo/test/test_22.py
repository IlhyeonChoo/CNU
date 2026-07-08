import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_22 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        A = np.random.randint(0, 10, size=(5, 5))
        res = solution(A)
        A = A.round().astype(np.int32)
        res = res.round().astype(np.int32)
        assert (np.sum(res - A, axis=0) == 10).all()


