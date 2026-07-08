import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_05 import solution


def test_solution():
    my_dict = {
        "orange": 5,
        "mango": 2,
        "apple": 19,
    }
    res = solution(my_dict)

    assert res == 5 + 2 + 19

    my_dict = {
        "pineapple": 115,
        "durian": 32,
        "grape": 13,
    }
    res = solution(my_dict)

    assert res == 115 + 32 + 13

    my_dict = {
        "watermelon": 15,
        "melon": 391,
        "blueberry": 19,
    }
    res = solution(my_dict)

    assert res == 15 + 391 + 19


