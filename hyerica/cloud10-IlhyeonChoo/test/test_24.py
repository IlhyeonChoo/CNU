import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_23 import *
from question_24 import *

def test():
    war = Warrior("홍길동", 1, base_hp=100, base_mp=50)
    mag = Mage("성춘향", 2, base_hp=50, base_mp=100)

    assert war.hp == 100+1*20
    assert war.mp == 50+1*5
    war.attack()
    assert war.damage > 0

    party = Party("전설의 용사단")
    party.add_member(war)
    party.add_member(mag)

    quest = Quest("고대 유적 탐험", 4)

    assert str(party) == "전설의 용사단 (2명)"
    assert str(quest) == "고대 유적 탐험 (Lv.4 이상)"

    assert quest.can_accept(war) == False