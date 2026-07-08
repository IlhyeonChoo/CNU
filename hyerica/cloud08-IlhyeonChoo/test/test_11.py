import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_11 import modify_tuple_list

def test():
    # 기본 케이스: 첫 번째 리스트의 두 번째 원소 수정
    t = ([1, 2, 3], 'hello')
    result = modify_tuple_list(t, 0, 1, 99)
    assert result == ([1, 99, 3], 'hello')
    assert result is t  # 튜플 자체는 같은 객체

    # 두 번째 리스트의 첫 번째 원소 수정
    t2 = ([10, 20], [30, 40])
    result2 = modify_tuple_list(t2, 1, 0, 99)
    assert result2 == ([10, 20], [99, 40])
    assert result2 is t2

    # 수정된 값이 문자열
    t3 = (['a', 'b', 'c'], [1, 2])
    result3 = modify_tuple_list(t3, 0, 2, 'z')
    assert result3[0] == ['a', 'b', 'z']
    assert result3 is t3

    # 첫 번째 원소 수정
    t4 = ([10, 20, 30],)
    result4 = modify_tuple_list(t4, 0, 0, 0)
    assert result4[0][0] == 0
    assert result4 is t4

    # 마지막 원소 수정
    t5 = ([100, 200, 300], 'x')
    result5 = modify_tuple_list(t5, 0, 2, 999)
    assert result5[0] == [100, 200, 999]

    # 튜플은 변경 불가지만 내부 리스트 id는 유지됨
    t6 = ([1, 2], [3, 4])
    inner_list_id = id(t6[0])
    modify_tuple_list(t6, 0, 0, 7)
    assert id(t6[0]) == inner_list_id  # 리스트 객체 자체는 그대로
    assert t6[0][0] == 7
