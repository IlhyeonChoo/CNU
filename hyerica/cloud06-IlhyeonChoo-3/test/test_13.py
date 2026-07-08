import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_13 import solution

def test():
    assert solution({'a': 1, 'b': 2}, {'b': 3, 'c': 4, 'd': 5}) == {'a': 1, 'b': 5, 'c': 4, 'd': 5}
    assert solution({'a': 1, 'b': 2}, {'a':2, 'b': 3, 'c': 4, 'd': 5}) == {'a': 3, 'b': 5, 'c': 4, 'd': 5}
