import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np

from question_04 import solution


def test_solution():
    for _ in range(10):
        a, b = np.random.randint(-10, 10, size=2)
        a = a + 1 if a == 0 else a
        steps = np.random.randint(10, 100)

        x, y = solution(a, b, steps)

        assert x.shape == (steps,)
        assert y.shape == (steps,)
        assert abs(x[0] - 0) < 1e-4 and abs(x[-1] - 10) < 1e-4
        assert abs((x[1:] - x[:-1]).mean() - 10 / (steps - 1)) < 1e-4
        assert np.all(np.abs(x**2*a + b - y) < 1e-4)


