import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_05 import modify_list

def test_list_modification():
    modified_list = modify_list()
    res = " ".join(map(lambda s: s.strip().lower(), modified_list))
    assert res == "My favorite programming language is Python . It has a dynamic type-checking system .".lower()

