import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_19 import solution

def test():
    assert solution("abbac") == "c"
    assert solution("accab") == "b"

