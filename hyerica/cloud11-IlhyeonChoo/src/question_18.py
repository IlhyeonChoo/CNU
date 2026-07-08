import numpy as np

def find_positive_positions(arr):
    """
    주어진 2차원 배열에서 0보다 큰 값이 있는 모든 위치(row, col)를 튜플의 리스트로 반환하세요.
    - 입력값:
        - arr (np.ndarray): 2차원 정수 배열
    - 반환값:
        - List[Tuple[int, int]]: 조건을 만족하는 위치의 (행, 열) 좌표 리스트
    - 힌트:
        - np.where()를 사용하면 조건을 만족하는 위치를 구할 수 있습니다.
    - 출력 예시:
        >>> find_positive_positions(vector)
        >>> [(np.int64(0), np.int64(1)), (np.int64(1), np.int64(1))]
    """
    # ----- your code here -----
    rows, cols = np.where(arr > 0)
    return list(zip(rows, cols))
    # --------------------------

if __name__ == "__main__":
    vector = np.array([[0, 1], [-2, 3]])
    result = find_positive_positions(vector)
    print("0보다 큰 위치들:", result)