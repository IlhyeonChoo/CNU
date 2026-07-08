import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_17 import solution

def test():
    assert solution("name:John,age:30,job:dev") == {'name': 'John', 'age': '30', 'job': 'dev'}
    assert solution("name:Jane,age:20,job:dev") == {'name': 'Jane', 'age': '20', 'job': 'dev'}

