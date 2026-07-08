import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_04 import count_positive

test_case = {
    'case_1': ([31, -241, 3214, -312, 243], 3),
    'case_2': ([0, 0, 0], 0),
    'case_3': ([1, 2, 3, 4, 5], 5),
    'case_4': ([-1, -2, -3, -4], 0),
    'case_5': ([10, -10, 20, -20, 0], 2),
    'case_6': ([], 0),
    'case_7': ([100], 1),
    'case_8': ([0, -1, -2, 3], 1),
}

def test():
    for k, v in test_case.items():
        assert count_positive(v[0]) == v[1]