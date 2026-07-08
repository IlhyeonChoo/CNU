import numpy as np


def absolute_difference(a, b):
    """
    두 개의 1차원 정수 배열이 주어졌을 때, 각 위치별로 절댓값 차이를 계산한 배열을 반환하세요.
    - 입력값:
        - a (np.ndarray): 1차원 정수 배열
        - b (np.ndarray): a와 같은 길이의 1차원 정수 배열
    - 반환값:
        - np.ndarray: 절댓값 차이를 담은 1차원 배열
    - 출력 예시:
        >>> absolute_difference(a_vec, b_vec)
        >>> array([3 3 6])
    """
    # ----- your code here -----
    return np.abs(a - b)
    # --------------------------


if __name__ == "__main__":
    a_vec = np.array([5, 1, 9])
    b_vec = np.array([2, 4, 3])
    result = absolute_difference(a_vec, b_vec)
    print("절댓값 차이 배열:", result)