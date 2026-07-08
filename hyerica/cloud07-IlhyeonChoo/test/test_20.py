import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

import copy
from question_20 import return_True, return_False

def test():
    A = (1,2,3,['a','b','c'])
    B = (1,2,3,'a','b','c')
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    true_result = return_True(B, B_copy)
    false_result = return_False(A, A_copy)
    assert true_result == True
    assert false_result == False