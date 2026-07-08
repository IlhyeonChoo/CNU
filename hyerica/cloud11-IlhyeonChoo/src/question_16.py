import numpy as np


def set_positions(arr_shape, coords, value):
    """
    주어진 배열 크기(arr_shape)에 대해, 주어진 좌표 리스트(coords)에 해당하는 위치에만
    지정된 값(value)을 설정한 배열을 생성하세요. 나머지는 0으로 유지됩니다.
    - 인자:
        - arr_shape (Tuple[int, int]): 출력 배열의 크기 (행, 열)
        - coords (List[Tuple[int, int]]): 값이 설정될 위치 좌표 목록
        - value (int): 해당 위치에 채워질 정수 값
    - 반환값:
        - np.ndarray: 지정된 좌표에만 값이 채워진 2차원 정수 배열
    - 출력 예시:
        >>> set_positions((3, 3), [(0, 1), (2, 2)], 9)
        >>> [[0, 9, 0],
             [0, 0, 0],
             [0, 0, 9]]
    """
    # ----- your code here -----
    arr = np.zeros(arr_shape, dtype=int)
    if coords:
        rows, cols = zip(*coords)
        arr[rows, cols] = value
    return arr
    # --------------------------


if __name__ == "__main__":
    result = set_positions((3, 3), [(0, 1), (2, 2)], 9)
    print(result)