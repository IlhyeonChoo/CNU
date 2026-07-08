import os, sys, random
import numpy as np
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_23 import solution


def test_solution():
    np.random.seed(18)
    for _ in range(10):
        rank = np.random.randint(2, 5)
        A = np.random.randint(0, 10, size=[np.random.randint(2, 5) for _ in range(rank)])
        res = solution(A)
        A = A.round().astype(np.int32)
        res = res.round().astype(np.int32)
        target = (A.shape[-2] * (A.shape[-2] - 1))//2
        assert (np.sum(res - A, axis=-2) == target).all()

