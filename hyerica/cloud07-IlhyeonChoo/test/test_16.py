import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_16 import group_employees_by_dept

def test():
    E = [('Kim', 'HR', 2022), ('Lee', 'Dev', 2021), ('Park', 'Dev', 2022), ('Choi', 'HR', 2023), ('Jung', 'Dev', 2021)]
    assert group_employees_by_dept(E) == {'HR': [('Kim', 2022), ('Choi', 2023)], 'Dev': [('Lee', 2021), ('Park', 2022), ('Jung', 2021)]}
    