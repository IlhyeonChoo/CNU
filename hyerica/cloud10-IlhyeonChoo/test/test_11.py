import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_11 import Time


def test_solution():
    for _ in range(5):
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        t = Time(hour, minute, second)
        assert t.hour == hour and t.minute == minute and t.second == second

        t = Time.from_string(f"{hour:02d}:{minute:02d}:{second:02d}")
        assert t.hour == hour and t.minute == minute and t.second == second

