import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_08 import format_string


def test_solution():
    assert format_string("") == ""
    assert format_string("ABC") == "ABC"
    assert format_string("ABC", postfix="DEF") == "ABC DEF"
    assert format_string("ABC", prefix="DEF") == "DEF ABC"
    assert format_string("ABC", prefix="XYZ", postfix="DEF") == "XYZ ABC DEF"


