import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_09 import calculate


def test_solution():
    stdout_file = "resources/stdout_q9.txt"
    q9_in_file = "resources/q9_in.txt"
    q9_out_file = "resources/q9_out.txt"

    with open(stdout_file, "w", encoding="utf-8") as sys.stdout, open(q9_in_file, "r", encoding="utf-8") as sys.stdin:
        calculate()

    with open(stdout_file, "r", encoding="utf-8") as f1, open(q9_out_file, "r", encoding="utf-8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    lines1 = list(filter(lambda l: len(l) > 0, map(lambda l: l.strip(), lines1)))
    lines2 = list(filter(lambda l: len(l) > 0, map(lambda l: l.strip(), lines2)))

    assert len(lines1) == len(lines2)

    for l1, l2 in zip(lines1, lines2):
        assert abs(float(l1.strip()) - float(l2.strip())) < 1e-4


