import copy
from collections import namedtuple

def copy_and_modify(name, members, new_member):
    """
    Team namedtuple(name, members)을 깊은 복사(deep copy)하고,
    복사본의 members 리스트에 new_member를 추가한 후,
    원본의 members 리스트와 복사본의 members 리스트를 튜플로 묶어 반환하는 함수이다.
    함수 내에서 'name', 'members' 필드를 가지는 Team namedtuple을 정의하시오.
    (힌트: namedtuple은 불변이지만 내부의 리스트는 가변이다.
           copy.deepcopy()로 완전히 독립적인 복사본을 만들어야 원본에 영향이 없다)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      name: 팀 이름 (문자열)
      members: 팀원 이름 리스트
      new_member: 복사본에 추가할 새 팀원 이름
    인자:
      name (str): 팀 이름
      members (list): 팀원 이름 리스트
      new_member (str): 복사본에 추가할 새 팀원 이름
    반환값:
      tuple: (원본_members_리스트, 복사본_members_리스트)
             원본은 변경되지 않고, 복사본에만 new_member가 추가되어 있어야 한다
    예시:
      >>> copy_and_modify('Alpha', ['Alice', 'Bob'], 'Charlie')
          (['Alice', 'Bob'], ['Alice', 'Bob', 'Charlie'])
    """
    # ===== Your Code Here =====
    Team = namedtuple('Team', ['name', 'members'])
    original_team = Team(name, members)
    copied_team = copy.deepcopy(original_team)
    copied_team.members.append(new_member)
    return original_team.members, copied_team.members
    # ==========================

if __name__ == '__main__':
    #### 함수 호출 ####
    original_members, copied_members = copy_and_modify('Alpha', ['Alice', 'Bob'], 'Charlie')
    print(f'원본 members: {original_members}')
    print(f'복사본 members: {copied_members}')
    #################
