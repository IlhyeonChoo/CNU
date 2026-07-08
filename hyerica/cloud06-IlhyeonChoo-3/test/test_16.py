import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_16 import solution

def test():
    assert solution("the quick brown fox jumps over the lazy dog the quick fox") == {'quick': 2, 'brown': 1, 'fox': 2, 'jumps': 1, 'lazy': 1, 'dog': 1}
    assert solution("the quick brown fox jumps over the lazy dog the quick") == {'quick': 2, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1}

