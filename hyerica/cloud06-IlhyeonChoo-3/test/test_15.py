import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_15 import solution

def test():
    assert solution(['a', 'b', 'c', 'd']) == {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
    assert solution(['e', 'f', 'g', 'h']) == {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H'}

