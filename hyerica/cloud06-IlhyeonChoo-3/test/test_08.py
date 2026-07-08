import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_08 import solution


def test_solution():
    my_dict = {
        "apple": 2,
        "orange": 3,
        "pineapple": 10,
        "pear": 9,
        "mango": 5,
    }
    res = solution(my_dict, "apple")
    assert res == 2

    my_dict = {
        "t-shirts": 39,
        "long pants": 21,
        "jeans": 30,
        "shoes": 4,
        "hat": 59,
    }
    res = solution(my_dict, "hat")
    assert res == 59

    my_dict = {
        "user_laptop": 31,
        "user_desktop": 20,
        "user_tablet": 13,
    }
    res = solution(my_dict, "user_desktop")
    assert res == 20


