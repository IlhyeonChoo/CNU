import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_02 import solution

test_case = {
    'case_1': ([1, '2', 3.5, True, False, '4'], 11.5),      
    'case_2': (['10', '20', '30'], 60),                    
    'case_3': ([True, True, False, 1, 0], 3),              
    'case_4': ([0, 0.0, '0', False], 0.0),                 
    'case_5': ([5, '5', 5.5], 15.5),                                              
    'case_6': (['100', True, 1.1, 2], 104.1),              
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]