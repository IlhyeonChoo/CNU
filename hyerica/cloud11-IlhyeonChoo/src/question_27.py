import numpy as np


def solution(M):
    """
    (n, d) 모양의 넘파이 행렬 M이 주어졌다고 가정합니다.
    이때, 행렬의 각 열에 대한 평균을 계산하세요.
    계산결과는 각 열의 평균을 저장한 (d,) 모양의 벡터가 나와야 합니다.

    인자:
        - M: (n, d) 모양의 넘파이 행렬
    반환값:
        - mean: (d,) 모양의 평균벡터

    예상출력:
        [0.12141585 0.38555284 0.32373106]
        [ 0.3381998   0.5380917  -0.63503216]
        [ 0.04270138 -0.01800666  0.42345216]
    """

    # ----- Your code here -----
    
    mean = np.mean(M, axis=0)
    # --------------------------

    return mean


if __name__ == "__main__":
    np.random.seed(13)
    M = np.random.randn(5, 3)
    print(solution(M))
    
    M = np.random.randn(5, 3)
    print(solution(M))
    
    M = np.random.randn(5, 3)
    print(solution(M))
