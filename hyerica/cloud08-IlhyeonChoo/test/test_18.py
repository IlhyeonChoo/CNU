import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_18 import unique_coordinates, closest_to_origin

def test():
    # 기본 케이스: 중복 제거 후 정렬
    assert unique_coordinates([(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]) == [(1, 2), (3, 4), (5, 6)]
    assert unique_coordinates([(0, 0), (0, 0), (1, 1)]) == [(0, 0), (1, 1)]

    # 중복 없는 경우 → 정렬만
    assert unique_coordinates([(3, 3), (1, 1), (2, 2)]) == [(1, 1), (2, 2), (3, 3)]

    # 모두 같은 좌표
    assert unique_coordinates([(5, 5), (5, 5), (5, 5)]) == [(5, 5)]

    # 원소 1개
    assert unique_coordinates([(0, 0)]) == [(0, 0)]

    # 결과 타입이 리스트, 각 원소는 튜플
    result = unique_coordinates([(2, 3), (1, 4)])
    assert isinstance(result, list)
    assert isinstance(result[0], tuple)

    # closest_to_origin 기본 케이스
    # (1,1): 2, (0,2): 4, (3,4): 25, (5,0): 25
    assert closest_to_origin([(3, 4), (1, 1), (5, 0), (0, 2)]) == (1, 1)

    # (2,2): 8, (3,0): 9, (0,5): 25
    assert closest_to_origin([(0, 5), (3, 0), (2, 2)]) == (2, 2)

    # 원점에 가장 가까운 점이 원점 자체인 경우
    assert closest_to_origin([(0, 0), (1, 1), (2, 2)]) == (0, 0)

    # 수평/수직 거리
    assert closest_to_origin([(0, 3), (4, 0)]) == (0, 3)  # 9 < 16

    # 원소가 1개
    assert closest_to_origin([(7, 7)]) == (7, 7)
