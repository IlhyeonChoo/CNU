import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_18 import solution

def test():
    assert solution("the quick brown fox") == ['the', 'quick', 'brown', 'fox']
    assert solution("the quick red fox jumps") == ['the', 'quick', 'red', 'fox', 'jumps']

