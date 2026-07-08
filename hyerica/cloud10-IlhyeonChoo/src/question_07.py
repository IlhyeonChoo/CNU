"""
question_06에서 구현한 Character 클래스를 복사해오세요. (임포트 하지마세요)
Character라는 이름의 클래스에 추가적으로 다음 두 개의 메서드를 구현하세요.

메서드1: move_to
    두 개의 정수로 이루어진 튜플 new_position을 입력받고 멤버변수 position을 업데이트하세요.

    인자:
        - new_position: 캐릭터의 새로운 위치, 정수 두 개로 이루어진 튜플형식
    반환값:
        - 없음

    예:
        character1 = Character("Jane", (0, 0), 100)
        print(character1.position)
        character1.move_to((1, 0))
        print(character1.position)

        의 결과는
        (0, 0)
        (1, 0)
        이 되어야 합니다.

메서드2: set_hp
    하나의 정수 new_hp를 입력받아 멤버변수 hp를 업데이트하는 메서드를 구현하세요.

    인자:
        - new_hp: 업데이트될 캐릭터의 체력, 정수형식
    반환값:
        - 없음

    예:
        character1 = Character("Jane", (0, 0), 100)
        print(character1.hp)
        character1.set_hp(120)
        print(character1.hp)

        의 결과는
        100
        120
        이 되어야 합니다.

예상출력:
    Character Jane is located at (1, 0) and has 100 HP.
    Character Henry is located at (99, 99) and has 79 HP.
"""

# ----- your code here -----
class Character:

    def __init__(self, name, initial_position, hp):
        self.name = name
        self.position = initial_position
        self.hp = hp

    def move_to(self, new_position):
        self.position = new_position

    def set_hp(self, new_hp):
        self.hp = new_hp

    def print_character(self):
        print(f"Character {self.name} is located at {self.position} and has {self.hp} HP.")


# --------------------------


if __name__ == "__main__":
    character1 = Character("Jane", (0, 0), 100)
    character2 = Character("Henry", (100, 100), 80)

    character1.move_to((1, 0))
    character2.move_to((99, 99))
    character2.set_hp(79)

    character1.print_character()
    character2.print_character()
