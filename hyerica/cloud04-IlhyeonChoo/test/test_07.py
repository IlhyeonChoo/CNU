import os, sys
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, 'src'))

from question_07 import solution

test_case = {
'case_1': ([{"name": "Alice", "skills": ["Python", "C++"], "experience": 5, "github": True},
         {"name": "Bob", "skills": ["Java", "Python"], "experience": 2, "github": False},
         {"name": "Charlie", "skills": ["Python", "JavaScript"], "experience": 4, "github": True}],
        ['Alice', 'Charlie']
    ),
    'case_2': (
        [
            {"name": "Dana", "skills": ["Python"], "experience": 1, "github": True},
            {"name": "Eve", "skills": ["C++", "Python"], "experience": 3, "github": False}
        ],
        []
    ),
    'case_3': (
        [
            {"name": "Frank", "skills": ["Python"], "experience": 3, "github": True}
        ],
        ['Frank']
    ),            
}

def test():
    for k, v in test_case.items():
        cands = solution(v[0])
        for i in v[1]:
            if i in cands:
                continue
            else:
                raise AssertionError()