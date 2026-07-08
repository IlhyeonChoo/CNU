"""
다음 세개의 캐릭터를 생성한 후, 주어진 출력과 같도록 프린트문을 완성하세요. 이때, 생성한 캐릭터의 멤버변수를 참조하여 코드를 작성하세요.

character1 (변수명)
    - name: 'Jane'
    - initial_position: (10, 10)
    - hp: 100
character2 (변수명)
    - name: 'Robert'
    - initial_position: (5, 10)
    - hp: 150
character3 (변수명)
    - name: 'David'
    - initial_position: (50, 50)
    - hp: 120

출력:
    Jane
    (5, 10)
    120
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
    # ----- your code here -----
    character1 = Character("Jane", (10, 10), 100)
    character2 = Character("Robert", (5, 10), 150)
    character3 = Character("David", (50, 50), 120)

    print(character1.name)
    print(character2.position)
    print(character3.hp)
    # --------------------------


if __name__ == "__main__":
    main()
