import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_01 import solution


def test_solution():
    assert solution(1, 10) == 55
    assert solution(2, 11) == 65
    assert solution(33, 44) == 462


