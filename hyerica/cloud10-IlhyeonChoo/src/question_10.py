"""
다음 다섯개의 캐릭터를 생성하고, characters 리스트에 추가하세요.
그리고, hp가 100을 초과하는 캐릭터만 골라오는 코드를 작성하세요(정확히 100 이면 제외).
filter 함수를 이용하세요.

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
    Character Robert is located at (5, 10) and has 150 HP.
    Character David is located at (50, 50) and has 120 HP.
    Character Rose is located at (0, 0) and has 110 HP.
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

    filtered_characters = filter(lambda character: character.hp > 100, characters)
    # --------------------------

    for c in filtered_characters:
        c.print_character()


if __name__ == "__main__":
    main()
