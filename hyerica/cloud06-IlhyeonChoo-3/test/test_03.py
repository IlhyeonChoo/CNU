import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_03 import solution


def test_solution():
    my_dict = {
        "orange": 5,
        "mango": 2,
        "apple": 19,
    }
    res = solution(my_dict)

    assert len(res) == 3
    assert "orange" in res and "mango" in res and "apple" in res

    my_dict = {
        "pineapple": 115,
        "durian": 32,
        "grape": 13,
    }
    res = solution(my_dict)

    assert len(res) == 3
    assert "pineapple" in res and "durian" in res and "grape" in res

    my_dict = {
        "watermelon": 15,
        "melon": 391,
        "blueberry": 19,
    }
    res = solution(my_dict)

    assert len(res) == 3
    assert "watermelon" in res and "melon" in res and "blueberry" in res


