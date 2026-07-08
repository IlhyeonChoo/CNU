import numpy as np


def solution(x, y):
    """
    두 넘파이 벡터 x, y가 주어졌을 때, 두 벡터 사이의 유클리드 거리를 구하는 코드를 작성하세요.
    벡터 사이의 유클리드 거리는 우리가 흔히 아는, 각 원소의 차이를 구한 후, 제곱하여 더해주고 제곱근을 구한 것입니다.
    벡터 x, y는 항상 rank=1짜리 넘파이 배열임을 가정합니다. 두 벡터의 길이는 항상 같다고 가정합니다.

    인자:
    - x: (n,) 모양의 벡터
    - y: (n,) 모양의 벡터

    반환값:
    - dist: x와 y사이의 유클리드 거리

    예상출력: (소수점 아래 작은 오차는 생길 수 있습니다)
        5.0
        14.422205101855956
        5.656854249492381
    """

    # ----- Your code here -----
    
    dist = np.sqrt(np.sum((x - y) ** 2))
    # --------------------------

    return dist


if __name__ == "__main__":
    x = np.array([0, 3])
    y = np.array([4, 0])
    print(solution(x, y))

    x = np.array([0, 8])
    y = np.array([12, 0])
    print(solution(x, y))
    
    x = np.array([0, -4])
    y = np.array([4, 0])
    print(solution(x, y))
