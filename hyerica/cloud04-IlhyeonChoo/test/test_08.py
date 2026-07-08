import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_08 import solution

test_case = {
    'case_1': ([7, 2, 5, 10, 1], [[1, 2], [5, 7, 10]]),
    'case_2': ([7, 2, 5, 10], [[2, 5], [7, 10]]),      
    'case_3': ([5], [[], [5]]),                        
    'case_4': ([], [[], []]),
    'case_5': ([9, 3, 6, 12, 4], [[3, 4], [6, 9, 12]]),
    'case_6': ([20, 1, 15, 8], [[1, 8], [15, 20]]),
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]
