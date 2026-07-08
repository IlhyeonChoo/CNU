from question_23 import *
from question_24 import *

class Monster:
    """
    전투 대상인 몬스터 정보를 저장하는 클래스
    생성자:
        - name (str): 몬스터 이름
        - hp (int): 최대 체력
        - current_hp (int): 현재 체력 (초기값은 최대 체력과 동일)
    메서드:
        - is_alive:
            - 반환값 (bool): current_hp가 0 보다 크면 True
        - take_damage:
            - dmg (int): 입을 피해량
            - current_hp를 감소시키고, 피해 메시지를 출력 (현재 체력 업데이트: max(current_hp - dmg, 0))
            - 예시: 불의 드래곤이(가) 12의 피해를 입었습니다. (남은 HP: 38)
    """

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.current_hp = hp

    def is_alive(self):
        return self.current_hp > 0

    def take_damage(self, dmg):
        self.current_hp = max(self.current_hp - dmg, 0)
        print(f"{self.name}이(가) {dmg}의 피해를 입었습니다. (남은 HP: {self.current_hp})")

class Battle:
    """
    파티와 몬스터 간의 전투를 관리하는 클래스
    생성자:
        - party (Party): 전투에 참여할 파티 객체
        - monster (Monster): 전투 대상이 될 몬스터 객체
    메서드:
        - battle:
            - 반환값 없음
            - While 문을 사용하여 몬스터의 체력이 0이 될때 까지 반복
            1. 반복문을 통해 파티원들이 차례로 몬스터를 공격
                - party.members 리스트를 활용
                - Warrior, Mage 클래스의 attack 메서드를 호출하여 데미지를 저장하고 공격 메시지를 출력
            2. 몬스터의 take_damage 메서드를 호출하여 몬스터의 체력을 감소
            3. is_alive 메서드를 호출하고 몬스터의 HP가 0 이하가 되면 전투 종료 메시지 출력하고 함수를 종료 (return)
            - 예시 출력:
              [전투 시작!] 전설의 용사단 vs 불의 드래곤
              --- 턴 1 ---
              전사 이몽룡이(가) 검으로 7 데미지를 주었습니다!
              불의 드래곤이(가) 7의 피해를 입었습니다. (남은 HP: 43)
              마법사 성춘향이(가) 마법으로 9 데미지를 주었습니다!
              불의 드래곤이(가) 9의 피해를 입었습니다. (남은 HP: 34)
              --- 턴 2 ---
              전사 이몽룡이(가) 검으로 3 데미지를 주었습니다!
              불의 드래곤이(가) 3의 피해를 입었습니다. (남은 HP: 31)
              ...
    """

    def __init__(self, party, monster):
        self.party = party
        self.monster = monster

    def battle(self):
        print(f"[전투 시작!] {self.party.name} vs {self.monster.name}")
        turn = 1
        while self.monster.is_alive():
            print(f"--- 턴 {turn} ---")
            for member in self.party.members:
                member.attack()
                self.monster.take_damage(member.damage)
                if not self.monster.is_alive():
                    print(f"[전투 종료!] {self.monster.name} 처치 완료")
                    return
            turn += 1

if __name__ == '__main__':
    # question_18, question_19에서 구현한 Warrior, Mage, Party 클래스를 import 하여 재사용

    # 캐릭터 생성 및 파티 구성
    w = Warrior("이몽룡", 4, 180, 60)
    m = Mage("성춘향", 5, 100, 120)

    party = Party("전설의 용사단")
    party.add_member(w)
    party.add_member(m)

    # 몬스터 생성
    monster = Monster("불의 드래곤", hp=50)

    # 전투 개시
    b = Battle(party, monster)
    b.battle()
