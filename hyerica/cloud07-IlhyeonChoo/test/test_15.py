import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_15 import generate_team_dict

def test():
    S = [('Blue', 10), ('Red', 15), ('Blue', 5), ('Green', 20), ('Red', 10)]
    assert generate_team_dict(S) == {'Blue': 15, 'Red': 25, 'Green': 20}