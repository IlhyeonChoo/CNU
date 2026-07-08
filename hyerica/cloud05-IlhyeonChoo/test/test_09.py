import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_09 import solution

test_case = {
    'case_1': (
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
    ),
    'case_2': (
        [[1, 2],
         [3, 4]],
        [[3, 1],
         [4, 2]]
    ),
    'case_3': (
        [[5]],
        [[5]]
    ),
    'case_4': (
        [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9,  10, 11, 12],
         [13, 14, 15, 16]],
        [[13, 9,  5, 1],
         [14, 10, 6, 2],
         [15, 11, 7, 3],
         [16, 12, 8, 4]]
    ),
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]