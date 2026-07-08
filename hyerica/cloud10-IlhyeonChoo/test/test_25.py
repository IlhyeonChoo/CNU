import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_23 import *
from question_24 import *
from question_25 import *

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

    # 몬스터 생성
    monster = Monster("불의 드래곤", hp=50)

    # 전투 개시
    b = Battle(party, monster)
    b.battle()

    assert monster.current_hp == 0