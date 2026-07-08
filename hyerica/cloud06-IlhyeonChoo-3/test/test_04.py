import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_04 import solution


def test_solution():
    my_dict = {
        "orange": 5,
        "mango": 2,
        "apple": 19,
    }
    res = solution(my_dict, "orange")

    assert len(res) == 2
    assert "mango" in res and "apple" in res

    my_dict = {
        "pineapple": 115,
        "durian": 32,
        "grape": 13,
    }
    res = solution(my_dict, "grape")

    assert len(res) == 2
    assert "pineapple" in res and "durian" in res

    my_dict = {
        "watermelon": 15,
        "melon": 391,
        "blueberry": 19,
    }
    res = solution(my_dict, "melon")

    assert len(res) == 2
    assert "watermelon" in res and "blueberry" in res


