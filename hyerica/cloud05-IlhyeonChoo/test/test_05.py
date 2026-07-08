import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_05 import solution

test_case = {
    'case_1': ([1, 2, 2, 3, 4, 4, 4, 10, 4, 1, 9, 9, 43], 4),
    'case_2': ([1, 1, 1, 2, 2], 1),
    'case_3': ([10, 20, 30, 30, 30, 20, 15], 30), 
    'case_4': ([7], 7),
    'case_5': ([5, 5, 5, 5, 5], 5),
    'case_6': ([1, 2, 3, 4, 5, 1], 1),  
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]