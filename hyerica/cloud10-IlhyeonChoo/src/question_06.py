"""
Character라는 이름의 클래스를 구현하세요.
이때, Character 클래스는 다음과 같은 형태를 갖고 있어야 합니다.
모든 메서드 인자 설명에서 self는 생략하였지만, 메서드가 class method나 static method가 아닌 이상 반드시 첫 번째 인자는 self이어야 합니다.

이름: Character (앞글자 대문자)
멤버변수:
    - name: 캐릭터의 이름. 문자열형식
    - position: 캐릭터의 현재 위치, 정수 두 개로 이루어진 튜플형식
    - hp: 캐릭터의 현재 체력. 정수형식
메서드:
- __init__
    name, initial_position, hp 세 개의 인자를 받고, 각 인지를 이용해서 멤버변수 'name', 'position', 'hp'를 생성하고 인자로 초기화합니다.
    (position의 경우, 인자의 이름은 'initial_position', 멤버변수의 이름은 'position' 입니다)

    인자:
        - name: 캐릭터의 이름. 문자열형식
        - initial_position: 캐릭터의 초기 위치, 정수 두 개로 이루어진 튜플형식
        - hp: 캐릭터의 초기 체력. 정수형식
    반환값:
        - 없음

예상출력:
    Character Jane is located at (0, 0) and has 100 HP.
    Character Henry is located at (100, 100) and has 80 HP.
"""

# ----- your code here -----
# 1. class 이름 완성
# 2. __init__ 메서드 구현

class Character:

    def __init__(self, name, initial_position, hp):
        self.name = name
        self.position = initial_position
        self.hp = hp

    # print_character는 수정하지마세요.
    def print_character(self):
        print(f"Character {self.name} is located at {self.position} and has {self.hp} HP.")
# --------------------------

if __name__ == "__main__":
    character1 = Character("Jane", (0, 0), 100)
    character2 = Character("Henry", (100, 100), 80)

    character1.print_character()
    character2.print_character()
