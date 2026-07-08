import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_08 import solution

test_case = {'case_1': [['The', 'quick', 'brown', 'fox', '.'], 3, ['quick', 'brown']],
 'case_2': [['elephant', 'giraffe', 'dolphin'], 4, ['elephant', 'giraffe', 'dolphin']],
 'case_3': [['a', 'ab', 'abc', 'abcd'], 1, ['ab', 'abc', 'abcd']],
 'case_4': [['Python', 'AI', 'deepLearning', 'GPT'], 3, ['Python', 'deepLearning']]}


def test():
    for k, v in test_case.items():
        # try:
        assert solution(v[0], v[1]) == v[2]
        # except AssertionError:
            # print(f"{k} failed")