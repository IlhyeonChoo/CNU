import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_06 import solution

test_case = {
    'case_1': [[1, 3, 4, 10, 4, 1, 43], [1, 3, 43]],
    'case_2': [[2, 4, 6, 8, 10], []],
    'case_3': [[5, 5, 5, 5], [5]],
    'case_4': [[2, 5, 2, 5, 3, 3, 9, 10], [5, 3, 9]],
    'case_5': [[2, 4, 6, 8, 11], [11]]
}


def test():
    for k, v in test_case.items():
        # try:
        assert solution(v[0]) == v[1]
        # except AssertionError:
            # print(f"{k} failed")