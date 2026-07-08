import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_12 import calculate_stats

def test():
    num_list = [1,2,3,4,5,6,7,8,9,10]
    assert calculate_stats(num_list) == (1, 10, 5.5)