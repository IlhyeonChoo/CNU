import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_12 import solution

def test():
    assert solution('Apple', {'Apple': 1000, 'Banana': 500, 'Orange': 800}) == 1000
    assert solution('Mango', {'Apple': 1000, 'Banana': 500, 'Orange': 800}) == None