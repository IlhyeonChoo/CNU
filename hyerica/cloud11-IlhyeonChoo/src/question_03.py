import numpy as np
import matplotlib.pyplot as plt


def solution(vec1, vec2):
    """
    두 벡터 vec1, vec2가 주어졌을 때, 내적을 구하는 코드를 작성하세요.
    이때, 두 벡터 vec1, vec2는 넘파이 배열이 아니라, 일반 파이썬 리스트입니다.
    1. 두 리스트를 넘파이 배열로 바꾸고,
    2. 두 넘파이 배열을 곱하고, 모든원소를 더해주는 방식으로 내적을 계산하세요.
    이때, 두 벡터 vec1, vec2의 길이는 항상 같다고 가정합니다.
    모양이 같은 두 넘파이 배열을 곱하거나 더하면 element-wise로 연산이 된다는 점을 이용하세요.

    인자:
        - vec1: 숫자들로 이루어진 파이썬 리스트(넘파이 배열 아님)
        - vec2: 숫자들로 이루어진 파이썬 리스트(넘파이 배열 아님)
    반환값:
        - 두 벡터의 내적값

    두 벡터를 곱한 후, 모든 원소의 합을 계산하고 싶은 경우, sum 함수를 이용하시면 됩니다.

    예상출력: (소수점 매우작은 오차는 생길 수 있습니다)
        14.400000000000002
        0.020000000000000004
        0.6799999999999999
    """

    # ----- your code here -----
    arr1 = np.array(vec1)
    arr2 = np.array(vec2)
    return np.sum(arr1 * arr2)

    # --------------------------


if __name__ == "__main__":
    vec1 = [1, 1, 3]
    vec2 = [-2.3, 1.1, 5.2]
    print(solution(vec1, vec2))

    vec1 = [-1.3, 5.2, 0.1]
    vec2 = [0.4, 0.1, 0.2]
    print(solution(vec1, vec2))

    vec1 = [3.3, 0.1]
    vec2 = [-0.1, 10.1]
    print(solution(vec1, vec2))
