import math
from collections import namedtuple

def create_points(data):
    """
    좌표 데이터(data)를 받아 Point namedtuple 리스트를 생성하는 함수이다.
    함수 내에서 'x', 'y' 필드를 가지는 Point namedtuple을 정의하고,
    입력된 데이터의 각 튜플을 Point 객체로 변환하여 리스트에 담아 반환한다.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      data: (x좌표, y좌표) 튜플의 리스트
    인자:
      data (list): (x, y) 형태의 튜플로 이루어진 리스트
    반환값:
      list: 각 요소가 Point namedtuple 객체인 리스트
    예시:
      >>> create_points([(0, 0), (3, 4)])
          [Point(x=0, y=0), Point(x=3, y=4)]
    """
    # ===== Your Code Here =====
    Point = namedtuple('Point', ['x', 'y'])
    return [Point(*point) for point in data]
    # ==========================

def get_distance(p1, p2):
    """
    두 Point namedtuple(p1, p2) 사이의 유클리드 거리를 계산하여 반환하는 함수이다.
    (힌트: math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2) 를 사용하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      p1: 첫 번째 Point namedtuple
      p2: 두 번째 Point namedtuple
    인자:
      p1 (Point): 첫 번째 좌표 Point namedtuple
      p2 (Point): 두 번째 좌표 Point namedtuple
    반환값:
      float: 두 점 사이의 유클리드 거리
    예시:
      >>> get_distance(Point(x=0, y=0), Point(x=3, y=4))
          5.0
    """
    # ===== Your Code Here =====
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
    # ==========================

if __name__ == '__main__':
    data = [(0, 0), (3, 4), (1, 1)]
    #### 함수 호출 ####
    points = create_points(data)
    print(f'좌표 목록: {points}')
    print(f'두 점 사이의 거리: {get_distance(points[0], points[1])}')
    #################
