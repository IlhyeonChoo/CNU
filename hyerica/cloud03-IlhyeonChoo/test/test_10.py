import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_10 import solution

test_case = {'case_1': [[19, 19, 15, 5, 5, 5, 1, 2], True],
 'case_2': [[5, 5, 5, 5, 5, 5, 5], False],
 'case_3': [[2, 3, 5, 5, 3, 5, 5, 3], True],
 'case_4': [[1, 2, 3, 4, 5, 6, 7, 8, 9], False],
 'case_5': [[43,19, 32, 22, 19, 19, 2, 19], False],
 'case_6': [[43,19, 32, 22, 19, 19, 2, 3], True],}

def test():
    for k, v in test_case.items():
        # try:
            assert solution(v[0]) == v[1]
        # except AssertionError:
        #     print(f"{k} failed")