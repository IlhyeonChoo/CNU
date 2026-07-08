import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np

from question_03 import solution


def test_solution():
    for _ in range(10):
        n = np.random.randint(3, 100)
        vec1, vec2 = np.random.rand(2, n)
        vec1 = vec1.tolist()
        vec2 = vec2.tolist()
        gt = sum([v1*v2 for v1, v2 in zip(vec1, vec2)])

        ret = solution(vec1, vec2)
        assert abs(gt - ret) < 1e-4

