import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_06 import solution

test_case = {
    'case_1': ("Artificial Intelligence is amazing", "amazing is Intelligence Artificial"),
    'case_2': ("Hello world", "world Hello"),
    'case_4': ("one two three four five", "five four three two one"),              
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]
