import sys, os, re
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_02 import convert_to_string

def test_conversion():
    assert convert_to_string(32.32).strip() == "32.32"
    assert convert_to_string(-13123).strip() == "-13123"
    assert convert_to_string(19283192389).strip() == "19283192389"