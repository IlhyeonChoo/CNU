import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_03 import solution

test_case = {
    'case_1': (23, 33, [24, 25, 26, 27, 28, 29, 30, 31, 32]),
    'case_2': (1, 5, [2, 3, 4]),
    'case_3': (10, 11, []),     
    'case_4': (10, 10, []),     
}

def test():
    for k, v in test_case.items():
        assert solution(v[0], v[1]) == v[2]