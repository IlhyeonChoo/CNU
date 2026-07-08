import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_14 import remove_duplicates, count_unique

def test():
    # 기본 케이스
    assert remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 2, 3, 4, 5, 6, 9]
    assert remove_duplicates([1, 1, 1, 2, 2, 3]) == [1, 2, 3]

    # 원소가 하나인 경우
    assert remove_duplicates([5]) == [5]

    # 이미 중복 없는 리스트 → 정렬만
    assert remove_duplicates([3, 1, 2]) == [1, 2, 3]

    # 모두 같은 값
    assert remove_duplicates([7, 7, 7, 7]) == [7]

    # 음수 포함
    assert remove_duplicates([-2, 0, -2, 1, 0]) == [-2, 0, 1]

    # count_unique: 완전히 겹치지 않는 두 리스트
    assert count_unique([1, 2, 3], [4, 5, 6]) == 6

    # count_unique: 완전히 같은 두 리스트
    assert count_unique([1, 1, 1], [1, 1]) == 1

    # count_unique: 일부 겹침
    assert count_unique([1, 2, 3, 2], [3, 4, 5, 4]) == 5

    # count_unique: 한 쪽이 다른 쪽의 부분집합
    assert count_unique([1, 2], [1, 2, 3, 4]) == 4

    # count_unique: 빈 리스트 포함
    assert count_unique([], [1, 2, 3]) == 3
    assert count_unique([1, 2], []) == 2
