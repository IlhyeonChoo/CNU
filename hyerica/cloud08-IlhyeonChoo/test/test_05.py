import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

import math
from question_05 import create_points, get_distance

def test():
    data = [(0, 0), (3, 4), (1, 1)]
    points = create_points(data)

    assert len(points) == 3
    assert points[0].x == 0 and points[0].y == 0
    assert points[1].x == 3 and points[1].y == 4
    assert points[2].x == 1 and points[2].y == 1

    # 3-4-5 직각삼각형
    assert get_distance(points[0], points[1]) == 5.0

    # 대각선 거리
    assert abs(get_distance(points[0], points[2]) - math.sqrt(2)) < 1e-9

    # 같은 점 → 거리 0
    p_same = create_points([(2, 3), (2, 3)])
    assert get_distance(p_same[0], p_same[1]) == 0.0

    # 수평 거리 (y 같음)
    p_horiz = create_points([(1, 5), (4, 5)])
    assert get_distance(p_horiz[0], p_horiz[1]) == 3.0

    # 수직 거리 (x 같음)
    p_vert = create_points([(7, 1), (7, 8)])
    assert get_distance(p_vert[0], p_vert[1]) == 7.0

    # 음수 좌표 포함
    p_neg = create_points([(-1, -1), (2, 3)])
    assert abs(get_distance(p_neg[0], p_neg[1]) - 5.0) < 1e-9  # sqrt(9+16)=5

    # 거리의 대칭성: d(a,b) == d(b,a)
    pa, pb = create_points([(0, 0)])[0], create_points([(3, 4)])[0]
    assert get_distance(pa, pb) == get_distance(pb, pa)
