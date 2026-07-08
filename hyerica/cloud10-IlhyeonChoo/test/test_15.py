import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_15 import main


def test_solution():
    stdout_file = "resources/stdout_q15.txt"
    q15_out_file = "resources/q15_out.txt"

    with open(stdout_file, "w", encoding="utf-8") as sys.stdout:
        main()

    with open(stdout_file, "r", encoding="utf-8") as f1, open(q15_out_file, "r", encoding="utf-8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    lines1 = list(filter(lambda l: len(l.strip()) > 0, lines1))
    lines2 = list(filter(lambda l: len(l.strip()) > 0, lines2))

    for l1, l2 in zip(lines1, lines2):
        assert l1.strip() == l2.strip()

