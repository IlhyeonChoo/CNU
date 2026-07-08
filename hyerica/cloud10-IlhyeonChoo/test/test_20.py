import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_20 import *

def test():
    item = Item("사이다", 2000, 2)
    assert str(item) == "사이다 (단가: 2000원, 수량: 2개)"

    # Setter
    item.quantity = 5
    item.price = 1000
    assert str(item) == "사이다 (단가: 1000원, 수량: 5개)"