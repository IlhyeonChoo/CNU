import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from itertools import product

from question_05 import solution


def test_solution():
    for _ in range(10):
        M = np.random.randint(5, 10)
        P = np.random.randint(1, (M - 1)//2)
        mat = np.random.randint(0, 100, size=M*M).reshape(M, M)

        mat_sliced = solution(mat, P)
        _matching(mat, mat_sliced)


def _matching(mat, mat_sliced):
    M = mat.shape[0]

    ret = np.array(list(map(lambda i: _slice_matching(mat, mat_sliced, i), range(M*M))))
    assert np.any(np.abs(ret - (mat_sliced*mat_sliced).sum()) < 1e-4)


def _slice_matching(mat, kernel, i):
    H, W = mat.shape
    kH, kW = kernel.shape
    
    h = i // W
    w = i % W

    mat_sliced = mat[h:h+kH, w:w+kW]
    if mat_sliced.shape == kernel.shape:
        return np.sum(mat_sliced * kernel)
    else:
        return -99999