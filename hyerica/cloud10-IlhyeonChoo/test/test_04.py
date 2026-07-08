import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_04 import solution


def test_solution():
    assert solution(["a", "b"]) == list(map(lambda s: s.upper(), ["a", "b"]))
    assert solution(["aaa", "bbbbb"]) == list(map(lambda s: s.upper(), ["aaa", "bbbbb"]))
    assert solution(["this", "is", "a", "simple", "sentence"]) == list(map(lambda s: s.upper(), ["this", "is", "a", "simple", "sentence"]))

