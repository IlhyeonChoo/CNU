import random 

class Character:
    """
    캐릭터의 기본 능력치를 정의하는 상위 클래스
    생성자:
        - name (str): 캐릭터 이름
        - _level (int): 캐릭터 레벨
        - _base_hp (int): 기본 체력
        - _base_mp (int): 기본 마나
         - _damage (int): 가장 최근의 공격 데미지를 저장하는 속성 (0으로 초기화) (매개변수 아님)
    메서드:
        - level (property):
            - _level 값을 반환
        - level (setter):
            - _level 값을 변경
        - damage (property):
            - _damage 값을 반환
        - damage (setter):
            - _damage 값을 변경
        - attack:
            - 기본 공격 동작을 출력
            - 예시: 홍길동 공격합니다!
        - __str__:
            - 반환값 (str): 캐릭터 정보를 문자열로 반환
            - 예시: 홍길동 (Lv.1) - HP: 100 / MP: 50
    """

    def __init__(self, name, level, base_hp, base_mp):
        self.name = name
        self._level = level
        self._base_hp = base_hp
        self._base_mp = base_mp
        self._damage = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def hp(self):
        return self._base_hp

    @property
    def mp(self):
        return self._base_mp

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def attack(self):
        print(f"{self.name} 공격합니다!")

    def __str__(self):
        return f"{self.name} (Lv.{self.level}) - HP: {self.hp} / MP: {self.mp}"
    
class Warrior(Character):
    """
    Character 클래스를 상속받아 구현한 전사 하위 클래스
    생성자:
        - 없음
    메서드:
        - hp (property):
            - 반환값 (int): base_hp + level * 20
        - mp (property):
            - 반환값 (int): base_mp + level * 5
        - attack:
            - 무기 공격 방식으로 데미지를 주는 행동을 출력
            - 함수 내부에서 데미지를 1~10 랜덤으로 설정 random.randint(1, 10)
            - 예시: 전사 홍길동이(가) 검으로 7 데미지를 주었습니다!
    """

    @property
    def hp(self):
        return self._base_hp + self.level * 20

    @property
    def mp(self):
        return self._base_mp + self.level * 5

    def attack(self):
        self.damage = random.randint(1, 10)
        print(f"전사 {self.name}이(가) 검으로 {self.damage} 데미지를 주었습니다!")

class Mage(Character):
    """
    Character 클래스를 상속받아 구현한 마법사 하위 클래스
    생성자:
        - 없음
    메서드:
        - hp (property):
            - 반환값 (int): base_hp + level * 8
        - mp (property):
            - 반환값 (int): base_mp + level * 25
        - attack:
            - 마법 공격 방식으로 데미지를 주는 행동을 출력
            - 함수 내부에서 데미지를 1~10 랜덤으로 설정 random.randint(1, 10)
            - 예시: 마법사 성춘향이(가) 마법으로 9 데미지를 주었습니다!
    """

    @property
    def hp(self):
        return self._base_hp + self.level * 8

    @property
    def mp(self):
        return self._base_mp + self.level * 25

    def attack(self):
        self.damage = random.randint(1, 10)
        print(f"마법사 {self.name}이(가) 마법으로 {self.damage} 데미지를 주었습니다!")

if __name__ == '__main__':
    war = Warrior("홍길동", 1, base_hp=100, base_mp=50)
    mag = Mage("성춘향", 2, base_hp=50, base_mp=100)

    print("전사:", war)
    war.attack()
    print("\n마법사:", mag)
    mag.attack()
