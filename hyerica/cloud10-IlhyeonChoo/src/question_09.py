"""
다음 다섯개의 캐릭터를 생성하고, characters 리스트에 추가하세요.
주어진 출력과 같도록 적절한 객체의 메서드를 호출하세요.
출력은 print_character 메서드를 이용합니다.

character1
    - name: 'Jane'
    - initial_position: (10, 10)
    - hp: 100
character2
    - name: 'Robert'
    - initial_position: (5, 10)
    - hp: 150
character3
    - name: 'David'
    - initial_position: (50, 50)
    - hp: 120
character3
    - name: 'Rose'
    - initial_position: (0, 0)
    - hp: 110
character3
    - name: 'Noah'
    - initial_position: (70, 10)
    - hp: 50

출력:
    Character Robert is located at (10, 10) and has 150 HP.
    Character Robert is located at (12, 12) and has 150 HP.
    Character Rose is located at (5, 5) and has 105 HP.

참고:
    각 출력 전에 해야 할 일은,
    1. Robert 이름을 가진 캐릭터의 위치를 수정해야 함
    2. Robert 이름을 가진 캐릭터의 위치를 수정해야 함
    3. Rose 이름을 가진 캐릭터의 위치와 체력을 수정해야 함

    멤버변수에 값 직접 대입하지 마시고, 메서드를 이용하세요.

"""

# ----- your code here -----
# question_07에서 구현한 Character 클래스를 복사해오세요. (임포트 하지마세요)
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


def main():
    characters = []
    # ----- your code here -----
    character1 = Character("Jane", (10, 10), 100)
    character2 = Character("Robert", (5, 10), 150)
    character3 = Character("David", (50, 50), 120)
    character4 = Character("Rose", (0, 0), 110)
    character5 = Character("Noah", (70, 10), 50)
    characters.extend([character1, character2, character3, character4, character5])

    character2.move_to((10, 10))
    character2.print_character()
    character2.move_to((12, 12))
    character2.print_character()
    character4.move_to((5, 5))
    character4.set_hp(105)
    character4.print_character()

    # --------------------------


if __name__ == "__main__":
    main()
