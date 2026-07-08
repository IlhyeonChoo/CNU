import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_19 import *

def test():
    menu = [
    Dessert("딸기 케이크", 4500, 350, 5),
    Drink("아이스 아메리카노", 3000, 5, 'M')
]
    assert str(menu) == "[MenuItem(name='딸기 케이크', price=4500, calories=350), MenuItem(name='아이스 아메리카노', price=3000, calories=5)]"
    assert str(menu[0]) == "[디저트] 딸기 케이크 - 4500원 / 350kcal (당도: 5)"