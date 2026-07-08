import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_09 import solution

test_case = {
    'case_1': ([1, 2, 3, 4, 5, 6], "단조 증가"),
    'case_2': ([6, 5, 4, 3, 2, 1], "단조 감소"),
    'case_3': ([1, 2, 3, 2, 5, 6], "단조 아님"),
    'case_4': ([5, 5, 5, 5], "단조 증가"),   
    'case_5': ([10, 9, 9, 9], "단조 감소"),  
    'case_6': ([1, 3, 2, 4], "단조 아님"),
    'case_8': ([2, 2, 3, 3, 4], "단조 증가"), 
    'case_9': ([9, 8, 8, 7, 7], "단조 감소"), 
}

def test():
    for k, v in test_case.items():
        assert solution(v[0]) == v[1]
        
