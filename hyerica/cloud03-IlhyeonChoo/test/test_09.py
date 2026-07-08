import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_09 import solution

test_case = {'case_1': ['The quick brown fox jumps over the lazy dog.', 36],
 'case_2': ['     a a a b b  c', 6],
 'case_3': ['AaBbCc', 6],
 'case_4': ['Hello, World!', 12],
 'case_5': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 49]}

def test():
    for k, v in test_case.items():
        # try:
        assert solution(v[0]) == v[1]
        # except AssertionError:
        #     print(f"{k} failed")