from question_23 import *

class Quest:
    """
    캐릭터가 수행할 수 있는 퀘스트 정보를 저장하는 클래스
    생성자:
        - title (str): 퀘스트 제목
        - min_level (int): 퀘스트 수락 최소 레벨
    메서드:
        - can_accept:
            - character (Character): 수락 조건을 확인할 캐릭터 객체
            - 반환값 (bool): 캐릭터 레벨이 최소 레벨 이상이면 True 아니면 False
        - assign:
            - character (Character): 퀘스트를 수락할 캐릭터 객체
            - 함수 내부에서 can_accept 함수를 호출하여 수락이 가능 여부 체크
            - 조건을 만족하면 수락 완료 메시지를 출력하고, 아니면 수락 불가 메시지를 출력
            - 예시:
              - 이몽룡 (Lv.3) : 수락 불가
              - 성춘향 (Lv.5) : 수락 완료
        - __str__:
            - 반환값 (str): 퀘스트 제목과 최소 레벨 정보를 문자열로 반환
            - 예시: 고대 유적 탐험 (Lv.4 이상)
    """

    def __init__(self, title, min_level):
        self.title = title
        self.min_level = min_level

    def can_accept(self, character):
        return character.level >= self.min_level

    def assign(self, character):
        result = "수락 완료" if self.can_accept(character) else "수락 불가"
        print(f"- {character.name} (Lv.{character.level}) : {result}")

    def __str__(self):
        return f"{self.title} (Lv.{self.min_level} 이상)"

class Party:
    """
    캐릭터들을 모아 파티를 구성하는 클래스
    생성자:
        - name (str): 파티 이름
        - members (list): 캐릭터 객체들을 저장할 빈 리스트로 초기화 (매개변수 아님)
    메서드:
        - add_member:
            - character (Character): 파티에 추가할 캐릭터 객체
            - members 리스트에 없다면 members 리스트에 추가
        - __len__:
            - 반환값 (int): 현재 파티원 수
        - __str__:
            - 반환값 (str): 파티 이름과 인원 수를 문자열로 반환
            - 예시: 전설의 용사단 (2명)
        - assign_quest:
            - 파티원 전원에게 퀘스트를 할당 시도하고 수락 가능 여부에 따라 결과를 출력
            - 함수 내부에서 파티의 멤버 수 만큼 quest.assign 함수를 호출
            - quest (Quest): 배정할 퀘스트 객체
            - 예시 출력:
              [퀘스트 배정: 고대 유적 탐험 (Lv.4 이상)]
              - 이몽룡 (Lv.3) : 수락 불가
              - 성춘향 (Lv.5) : 수락 완료
    """

    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, character):
        if character not in self.members:
            self.members.append(character)

    def __len__(self):
        return len(self.members)

    def __str__(self):
        return f"{self.name} ({len(self)}명)"

    def assign_quest(self, quest):
        print(f"[퀘스트 배정: {quest}]")
        for member in self.members:
            quest.assign(member)

if __name__ == '__main__':
    # question_18에서 구현한 Warrior, Mage 클래스를 import 하여 재사용

    w = Warrior("이몽룡", 3, 200, 50)
    m = Mage("성춘향", 5, 100, 120)

    party = Party("전설의 용사단")
    party.add_member(w)
    party.add_member(m)

    quest = Quest("고대 유적 탐험", 4)

    print("파티:", party)
    print("퀘스트:", quest)
    party.assign_quest(quest)
