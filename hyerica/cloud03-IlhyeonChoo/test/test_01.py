import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_01 import compute_circle_area

def test_circle_area():
    assert abs(compute_circle_area(3) - 28.274328) < 1e-6
    assert abs(compute_circle_area(5) - 78.5398) < 1e-6
    assert abs(compute_circle_area(7) - 153.938008) < 1e-6

