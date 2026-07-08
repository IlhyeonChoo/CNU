import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_21 import *

def test():
    p = Person("홍길동", 175, 70)
    assert p.bmi == 22.9
    p.height = 100
    p.weight = 10
    assert p.height == 100
    assert p.weight == 10