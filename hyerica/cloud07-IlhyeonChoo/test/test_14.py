import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_14 import find_topk_items

def test():
    C = [['apple', 'banana', 'milk'], ['milk', 'bread'], ['apple', 'milk', 'egg'], ['banana', 'bread', 'milk']]
    K = 2
    assert find_topk_items(C, K) == [('milk', 4), ('apple', 2)]