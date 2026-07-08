import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_10 import solution

test_case = {
    'case_1': ("aaabbcaad", "a3b2c1a2d1"),
    'case_2': ("abc", "a1b1c1"),                  
    'case_3': ("a", "a1"),                        
    'case_4': ("zzzzzz", "z6"),                   
    'case_5': ("aabbccddeeff", "a2b2c2d2e2f2"),   
    'case_6': ("aabbaa", "a2b2a2"),               
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]
