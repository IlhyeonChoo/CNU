import numpy as np


def solution(v1, v2):
    """
    두 개의 random variable로부터 샘플링된 두 넘파이 배열 데이터셋 v1, v2가 주어졌을 떄, 두 random variable 사이의 covariance를 계산하세요.
    이때, v1, v2는 모두 n개의 데이터를 저장한 (n,) 모양의 rank=1 넘파이 배열입니다.
    
    covariance를 계산하는 과정은 다음과 같습니다.
    1. 각 배열의 평균을 계산
    2. 각 배열로부터 평균을 뺌
    3. 평균을 뺀 두 배열의 내적을 계산하고 n - 1로 나눔

    인자:
        - v1: (n,) 모양의 넘파이 배열
        - v2: (n,) 모양의 넘파이 배열

    반환값:
        - cov: v1와 v2사이의 covariance

    예상출력:
        -0.31941785928649363
        -0.13932718051780912
        -0.3746728403037274
    """

    n = v1.shape[0]
    
    # ----- Your code here -----
    
    cov = np.sum((v1 - np.mean(v1)) * (v2 - np.mean(v2))) / (n - 1)
    # --------------------------

    return cov


if __name__ == "__main__":
    np.random.seed(13)
    v1, v2 = np.random.randn(2, 5)
    print(solution(v1, v2))
    
    v1, v2 = np.random.randn(2, 7)
    print(solution(v1, v2))
    
    v1, v2 = np.random.randn(2, 9)
    print(solution(v1, v2))
