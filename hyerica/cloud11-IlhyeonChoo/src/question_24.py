import numpy as np


def solution(a, b):
    """
    두 벡터 a, b가 주어졌을 떄, 두 벡터의 코사인 유사도를 계산하세요.
    두 벡터의 코사인 유사도는 각 벡터를 정규화한 후 (크기 1로 만듦), 내적하면 계산할 수 있습니다.

    이때, 벡터를 정규화하는 과정은 벡터를 벡터의 크기로 나눠주면 됩니다.
    
    인자로 들어오는 두 벡터 a, b는 항상 rank=1의 벡터이며, 같은 길이의 벡터라고 가정합니다.

    인자:
        - a: (n,) 모양의 벡터
        - b: (n,) 모양의 벡터

    반환값:
        - cos_sim: a, b의 코사인 유사도

    예상출력: (매우 작은 소수점 오차는 발생할 수 있습니다)
        0.9999999999999999          (=1, 두 벡터가 평행)
        0.0                         (두 벡터가 수직)
        -0.09245003270420488
    """

    # ----- Your code here -----

    cos_sim = np.sum(a * b) / (np.sqrt(np.sum(a**2)) * np.sqrt(np.sum(b**2)))
    # --------------------------
    return cos_sim


if __name__ == "__main__":
    a = np.array([1, 2])
    b = np.array([2, 4])
    print(solution(a, b))

    a = np.array([1, 4, 2])
    b = np.array([1, -0.5, 0.5])
    print(solution(a, b))

    a = np.array([-1, -2, 2])
    b = np.array([-0.3, 0.2, 0])
    print(solution(a, b))
