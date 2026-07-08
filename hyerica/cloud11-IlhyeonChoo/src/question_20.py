import numpy as np

def l2_distance(points, query):
    """
    주어진 2차원 배열(points)의 각 행(좌표)과 기준점(query) 간의 유클리드 거리를 계산하고 반환하시오.
    - 입력값:
        - points (np.ndarray): (N, D) 크기의 점 배열
        - query (np.ndarray): (D,) 크기의 기준점 벡터
    - 반환값:
        - np.ndarray: (N,) 크기의 거리 벡터
    - 출력 예시:
        >>> l2_distance(pt, q)
        >>> array([1.         5.83095189 9.21954446])
    """
    # ----- your code here -----
    return np.sqrt(np.sum((points - query) ** 2, axis=1))
    # --------------------------

if __name__ == "__main__":
    pt = np.array([[1, 2], [4, 6], [7, 8]])
    q = np.array([1, 1])
    result = l2_distance(pt, q)
    print("거리 벡터:", result)