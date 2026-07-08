import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_11 import solution

def test():
    assert solution('Lora', {'Alice': 85, 'Bob': 92, 'Charlie': 78})[1] == '찾을 수 없음'
    assert solution('Bob', {'Alice': 85, 'Bob': 92, 'Charlie': 78})[1] == 92