import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np

from question_01 import solution


def test_solution():
    np.random.seed(16)
    zero_tensor, one_tensor, standarad_gaussian_tensor = solution()

    print(standarad_gaussian_tensor.mean(), standarad_gaussian_tensor.std())

    zero_tensor = zero_tensor.round().astype(np.int32)
    one_tensor = one_tensor.round().astype(np.int32)

    assert zero_tensor.shape == (2, 3) and zero_tensor.sum() == 0
    assert one_tensor.shape == (2, 3, 2) and one_tensor.sum() == 2*3*2
    assert standarad_gaussian_tensor.shape == (2, 4, 4) and abs(standarad_gaussian_tensor.mean() - -0.22335211137665942) < 1e-4 and abs(standarad_gaussian_tensor.std() - 1.018250641866084) < 1e-4