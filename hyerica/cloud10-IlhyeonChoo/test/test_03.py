import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_03 import solution


def test_solution():
    assert solution([3, 1, 34, 12, 3]) == sorted([3, 1, 34, 12, 3])
    assert solution([3, 1, 34, 12, 3], descending=True) == sorted([3, 1, 34, 12, 3], reverse=True)
    assert solution([5, 123, 4, 52]) == sorted([5, 123, 4, 52])
    assert solution([5, 123, 4, 52], descending=True) == sorted([5, 123, 4, 52], reverse=True)

