import sys, os, re
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_03 import add_prefix_to_string

def test_prefix_addition():
    res = add_prefix_to_string(string="world", prefix="hello ")
    res = re.sub(r"\s+", " ", res.strip())
    assert res == "hello world"

    res = add_prefix_to_string(string="ABCDE", prefix="EFGHI ")
    res = re.sub(r"\s+", " ", res.strip())
    assert res == "EFGHI ABCDE"

    res = add_prefix_to_string(string="python", prefix="I love ")
    res = re.sub(r"\s+", " ", res.strip())
    assert res == "I love python"
