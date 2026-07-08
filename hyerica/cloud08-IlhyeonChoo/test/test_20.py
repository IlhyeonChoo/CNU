import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_20 import copy_and_modify

def test():
    # 기본 케이스
    original_members, copied_members = copy_and_modify('Alpha', ['Alice', 'Bob'], 'Charlie')
    assert original_members == ['Alice', 'Bob']
    assert copied_members == ['Alice', 'Bob', 'Charlie']

    # 멤버가 3명인 경우
    original_members2, copied_members2 = copy_and_modify('Beta', ['X', 'Y', 'Z'], 'W')
    assert original_members2 == ['X', 'Y', 'Z']
    assert copied_members2 == ['X', 'Y', 'Z', 'W']

    # 원본과 복사본의 리스트 객체가 서로 다른 객체임을 확인 (deepcopy)
    orig, copy = copy_and_modify('Gamma', ['p', 'q'], 'r')
    assert orig is not copy  # 서로 다른 객체

    # 원본이 변경되지 않음을 직접 확인
    members_input = ['m1', 'm2']
    orig3, copy3 = copy_and_modify('Delta', members_input, 'new')
    assert 'new' not in orig3
    assert 'new' in copy3

    # 복사본에 new_member가 마지막에 추가됨
    orig4, copy4 = copy_and_modify('Team', ['a'], 'b')
    assert copy4[-1] == 'b'
    assert orig4 == ['a']

    # 빈 멤버 리스트에서 추가
    orig5, copy5 = copy_and_modify('Empty', [], 'first')
    assert orig5 == []
    assert copy5 == ['first']
