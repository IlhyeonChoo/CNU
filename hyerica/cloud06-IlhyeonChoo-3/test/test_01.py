import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_01 import solution


def test_solution():
    res = solution()
    keys = res.keys()
    assert len(keys) == 3
    assert "names" in keys and "age" in keys and "gender" in keys
    assert res["names"] == ["Alice", "Bob", "Charlie"]
    assert res["age"] == [29, 14, 22]
    assert res["gender"] == ["female", "male", "female"]



