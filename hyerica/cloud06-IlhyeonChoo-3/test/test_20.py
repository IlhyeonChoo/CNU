import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_20 import solution

def test():
    assert solution("hello world", "hezlo wprld")[0] == 8
    assert solution("hello world", "hezlo wprld")[1] == 2
    assert solution("hello world", "hezlo wprld")[2] == 2

    assert solution("hello world", "hello wprld")[0] == 9
    assert solution("hello world", "hello wprld")[1] == 1
    assert solution("hello world", "hello wprld")[2] == 6
