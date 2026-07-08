import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_14 import solution

def test():
    assert solution(["apple", "banana", "kiwi"]) == {'apple': 5, 'banana': 6, 'kiwi': 4}
    assert solution(["strawberry", "banana", "kiwi"]) == {'strawberry': 10, 'banana': 6, 'kiwi': 4}
