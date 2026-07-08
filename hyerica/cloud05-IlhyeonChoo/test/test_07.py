import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_07 import solution

test_case = {
    'case_1': (([3, 1, 5, 2, 8, 4, 6], 3), [5, 5, 8, 8, 8]), 
    'case_2': (([1, 3, 2, 5, 4],       2), [3, 3, 5, 5]),      
    'case_3': (([9, 8, 7, 6, 5],       4), [9, 8]),            
    'case_4': (([1, 1, 1, 1, 1],       3), [1, 1, 1]),         
    'case_5': (([4, 2, 6, 1, 3, 8, 5], 4), [6, 6, 8, 8]),      
}

def test():
    for k, (args, expected) in test_case.items():
        nums, window = args
        result = solution(nums, window)
        assert result == expected