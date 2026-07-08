import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_13 import Time


def test_solution():
    t1 = Time.from_string("12:30:23")
    t1.add(hour=2, minute=7, second=40)
    assert t1.hour == 14 and t1.minute == 38 and t1.second == 3

    t2 = Time.from_string("03:30:20")
    t1.add(other_time=t2)
    assert t1.hour == 18 and t1.minute == 8 and t1.second == 23

    t1.add(hour=2, minute=7, second=40)
    assert t1.hour == 20 and t1.minute == 16 and t1.second == 3

    t2 = Time.from_string("03:30:20")
    t1.add(other_time=t2)
    assert t1.hour == 23 and t1.minute == 46 and t1.second == 23

