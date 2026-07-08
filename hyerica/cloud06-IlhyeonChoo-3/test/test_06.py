import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_06 import solution


def test_solution():
    my_dict = {
        "orange": 5,
        "mango": 2,
        "apple": 19,
    }
    res = solution(my_dict, "pineapple", 312)

    keys = res.keys()
    assert len(keys) == 4
    assert "orange" in keys and "mango" in keys and "apple" in keys and "pineapple" in keys
    assert res["orange"] == 5
    assert res["mango"] == 2
    assert res["apple"] == 19
    assert res["pineapple"] == 312

    my_dict = {
        "pineapple": 115,
        "durian": 32,
        "grape": 13,
    }
    res = solution(my_dict, "apple", 1)

    keys = res.keys()
    assert len(keys) == 4
    assert "pineapple" in keys and "durian" in keys and "grape" in keys and "apple" in keys
    assert res["pineapple"] == 115
    assert res["durian"] == 32
    assert res["grape"] == 13
    assert res["apple"] == 1

    my_dict = {
        "watermelon": 15,
        "melon": 391,
        "blueberry": 19,
    }
    res = solution(my_dict, "grape", 11)

    keys = res.keys()
    assert len(keys) == 4
    assert "watermelon" in keys and "melon" in keys and "blueberry" in keys and "grape" in keys
    assert res["watermelon"] == 15
    assert res["melon"] == 391
    assert res["blueberry"] == 19
    assert res["grape"] == 11


