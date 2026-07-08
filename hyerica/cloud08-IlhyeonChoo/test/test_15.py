import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_15 import set_operations

def test():
    # 기본 케이스
    result = set_operations({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result['union'] == {1, 2, 3, 4, 5, 6}
    assert result['intersection'] == {3, 4}
    assert result['difference'] == {1, 2}

    # 문자열 원소
    result2 = set_operations({'a', 'b', 'c'}, {'b', 'c', 'd'})
    assert result2['union'] == {'a', 'b', 'c', 'd'}
    assert result2['intersection'] == {'b', 'c'}
    assert result2['difference'] == {'a'}

    # 교집합이 없는 경우
    result3 = set_operations({1, 2}, {3, 4})
    assert result3['union'] == {1, 2, 3, 4}
    assert result3['intersection'] == set()
    assert result3['difference'] == {1, 2}

    # s1이 s2의 부분집합인 경우 → 차집합 = 공집합
    result4 = set_operations({1, 2}, {1, 2, 3, 4})
    assert result4['difference'] == set()
    assert result4['intersection'] == {1, 2}

    # s2가 s1의 부분집합인 경우
    result5 = set_operations({1, 2, 3, 4}, {2, 3})
    assert result5['difference'] == {1, 4}
    assert result5['intersection'] == {2, 3}

    # 완전히 같은 두 집합
    result6 = set_operations({5, 6, 7}, {5, 6, 7})
    assert result6['union'] == {5, 6, 7}
    assert result6['intersection'] == {5, 6, 7}
    assert result6['difference'] == set()

    # 반환 딕셔너리 키 확인
    result7 = set_operations({1}, {2})
    assert 'union' in result7
    assert 'intersection' in result7
    assert 'difference' in result7
