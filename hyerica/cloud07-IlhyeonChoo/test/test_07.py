import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_07 import parse_string_to_int


def test_solution():
    for _ in range(5):
        n = random.randint(5, 10)
        int_list = [random.randint(10, 100) for _ in range(n)]
        str_list = [str(d) for d in int_list]
        assert parse_string_to_int(str_list) == int_list


