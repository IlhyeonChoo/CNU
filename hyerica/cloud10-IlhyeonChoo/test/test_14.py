import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_13 import Time
from question_14 import TimeComparator


def test_solution():
    assert TimeComparator.equals_hour(Time.from_string("09:00:00"), Time.from_string("09:02:30")) is True
    assert TimeComparator.equals_hour(Time.from_string("08:00:00"), Time.from_string("09:02:30")) is False
    assert TimeComparator.equals_hour_and_minute(Time.from_string("08:00:00"), Time.from_string("08:00:30")) is True
    assert TimeComparator.equals_hour_and_minute(Time.from_string("08:00:00"), Time.from_string("08:01:30")) is False
    assert TimeComparator.equals_hour(Time.from_string("21:00:00"), Time.from_string("21:02:30")) is True
    assert TimeComparator.equals_hour(Time.from_string("22:24:00"), Time.from_string("21:24:30")) is False
    assert TimeComparator.equals_hour_and_minute(Time.from_string("21:00:00"), Time.from_string("21:00:30")) is True
    assert TimeComparator.equals_hour_and_minute(Time.from_string("14:14:00"), Time.from_string("14:13:30")) is False

