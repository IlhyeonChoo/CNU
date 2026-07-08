import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_13 import unpack_first_rest_last, swap_with_unpack

def test():
    # 기본 케이스
    assert unpack_first_rest_last((1, 2, 3, 4, 5)) == (1, [2, 3, 4], 5)
    assert unpack_first_rest_last(('a', 'b', 'c')) == ('a', ['b'], 'c')
    assert unpack_first_rest_last((10, 20, 30)) == (10, [20], 30)

    # middle이 여러 개
    assert unpack_first_rest_last((0, 1, 2, 3, 4, 5, 6)) == (0, [1, 2, 3, 4, 5], 6)

    # first, last만 확인
    result = unpack_first_rest_last(('x', 'y', 'z', 'w'))
    assert result[0] == 'x'
    assert result[2] == 'w'
    assert result[1] == ['y', 'z']

    # middle 리스트 타입 확인
    r = unpack_first_rest_last((1, 2, 3))
    assert isinstance(r[1], list)

    # swap 기본 케이스
    assert swap_with_unpack(10, 20) == (20, 10)
    assert swap_with_unpack('hello', 'world') == ('world', 'hello')
    assert swap_with_unpack(1, 2) == (2, 1)

    # swap 다양한 타입
    assert swap_with_unpack(True, False) == (False, True)
    assert swap_with_unpack(3.14, 2.71) == (2.71, 3.14)
    assert swap_with_unpack([1, 2], [3, 4]) == ([3, 4], [1, 2])

    # swap 같은 값
    assert swap_with_unpack(5, 5) == (5, 5)
