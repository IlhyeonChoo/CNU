import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_07 import solution


def test_solution():
    for n in [10, 20, 30, 40, 50]:
        res = solution(n)
        keys = res.keys()

        assert len(keys) == n//2
        for i in range(0, n, 2):
            assert abs(res[i] - 3.14*i*2) < 1e-4


