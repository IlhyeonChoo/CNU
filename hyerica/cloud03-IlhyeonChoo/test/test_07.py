import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_07 import solution

test_case = {'case_1': [[1, 3, 79, 10, 4, 1, 39, 62, 103, 246], [79, 39, 103]],
 'case_2': [[7, 9, 13, 15, 79], [13, 15, 79]],
 'case_3': [[79, 39, 103, 79, 39, 103], [79, 39, 103, 79, 39, 103]]}


def test():
    for k, v in test_case.items():
        # try:
        assert solution(v[0]) == v[1]
        # except AssertionError:
            # print(f"{k} failed")