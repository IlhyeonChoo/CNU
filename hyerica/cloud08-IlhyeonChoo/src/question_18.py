def unique_coordinates(coords):
    """
    좌표 리스트(coords)에서 중복된 좌표를 제거하고 오름차순으로 정렬된 리스트를 반환하는 함수이다.
    튜플은 해시 가능(hashable)하므로 세트의 원소로 사용할 수 있다.
    (힌트: set()에 좌표 튜플을 넣어 중복을 제거하고, sorted()로 정렬하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      coords: (x, y) 형태의 좌표 튜플 리스트 (중복 포함 가능)
    인자:
      coords (list): (x, y) 형태의 좌표 튜플로 이루어진 리스트
    반환값:
      list: 중복이 제거된 좌표 튜플의 오름차순 정렬된 리스트
    예시:
      >>> unique_coordinates([(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)])
          [(1, 2), (3, 4), (5, 6)]
    """
    # ===== Your Code Here =====
    return sorted(set(coords))
    # ==========================

def closest_to_origin(coords):
    """
    좌표 리스트(coords)에서 원점(0, 0)에 가장 가까운 좌표 튜플을 반환하는 함수이다.
    거리는 x**2 + y**2 로 계산하시오 (제곱근 불필요).
    (힌트: min() 함수와 key 매개변수를 활용하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      coords: (x, y) 형태의 좌표 튜플 리스트
    인자:
      coords (list): (x, y) 형태의 좌표 튜플로 이루어진 리스트
    반환값:
      tuple: 원점에 가장 가까운 좌표 튜플
    예시:
      >>> closest_to_origin([(3, 4), (1, 1), (5, 0), (0, 2)])
          (1, 1)
    """
    # ===== Your Code Here =====
    return min(coords, key=lambda coord: coord[0] ** 2 + coord[1] ** 2)
    # ==========================

if __name__ == '__main__':
    coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4)]
    #### 함수 호출 ####
    print(f'중복 제거 좌표: {unique_coordinates(coords)}')
    print(f'원점에 가장 가까운 좌표: {closest_to_origin([(3, 4), (1, 1), (5, 0), (0, 2)])}')
    #################
