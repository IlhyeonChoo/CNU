import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_08 import solution

test_case = {
    'case_1': (([1, 2, 3, 1, 4, 2, 3], 6),  [[0, 2], [1, 3], [4, 5]]), 
    'case_2': (([1, 2, 3, 4, 5],       9),  [[1, 3], [3, 4]]),          
    'case_3': (([3, 3, 3, 3],          6),  [[0, 1], [1, 2], [2, 3]]),  
    'case_4': (([10, 1, 2, 3, 4],      10),  [[0, 0], [1, 4]]),         
    'case_5': (([1, 1, 1, 1, 1, 1],    3),   [[0, 2], [1, 3], [2, 4], [3, 5]]),   
}

def test():
    for k, (args, expected) in test_case.items():
        nums, target = args
        result = solution(nums, target)
        assert result == expected