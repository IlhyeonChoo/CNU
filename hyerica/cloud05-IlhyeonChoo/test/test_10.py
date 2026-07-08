import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_10 import solution

test_case = {
    'case_1': ([10, 9, 2, 5, 3, 7, 101, 18], 4),  
    'case_2': ([0, 1, 0, 3, 2, 3],            4),  
    'case_3': ([7, 7, 7, 7, 7],               1),  
    'case_4': ([1, 2, 3, 4, 5],               5),  
    'case_5': ([5, 4, 3, 2, 1],               1),  
    'case_6': ([3, 1, 4, 1, 5, 9, 2, 6],      4),  
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]