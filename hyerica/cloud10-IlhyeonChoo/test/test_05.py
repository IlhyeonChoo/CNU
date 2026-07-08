import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_05 import solution


def test_solution():
    assert solution([30, 132, 41, 1561, 134]) == list(filter(lambda n: len(str(n)) == 3, [30, 132, 41, 1561, 134]))
    assert solution([415, 561, 423, 1156]) == list(filter(lambda n: len(str(n)) == 3, [415, 561, 423, 1156]))
    assert solution([6, 14, 62, 1]) == list(filter(lambda n: len(str(n)) == 3, [6, 14, 62, 1]))

