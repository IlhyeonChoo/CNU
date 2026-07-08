import numpy as np
import matplotlib.pyplot as plt


def solution(x, gradient, y_intercept):
    """
    직선의 기울기(gradient), y 절편(y intercept)가 주어졌을 때,
    해당 직선을 지나면서 주어진 x축 값에 대응하는 y축 값을 구하여 반환하세요.

    이때, gradient, y_intercept는 각각 실수이며, x는 실수로 이루어진 1차원 넘파이 배열입니다.

    예를들어, gradient=1, y_intercept=2이고, x=np.array([1, 2, 3])로 주어진 경우,
    반환값 y는 np.array([3, 4, 5]) 이어야 합니다.

    참고:
    - for문을 사용하지 마세요.
    - 넘파이 배열에 어떤 실수 하나를 곱하거나 더하면, 배열 내 모든 원소에 각각 해당 실수가 똑같이 곱해지거나 더해집니다.
      예를들어, a = np.array([1, 2, 3]) 이 있을 때, a + 2는 np.array([3, 4, 5]) 와 같습니다.

    인자:
        - x: (n,) 차원의 넘파이 배열(실수타입). x축 좌표들
        - gradient: 실수 하나. 직선의 기울기
        - y_intercept: 실수 하나. 직선의 y 절편

    반환값:
        - y: (n,) 차원의 넘파이 배열(실수타입). x축 좌표에 대응하는 y축 좌표들

    예상출력:
        [ 4  6  8 10 12]
        [ 3  2  1  0 -1]
        [  4  -6 -16 -26 -36]
    """
    
    # ----- your code here -----
    y = x * gradient + y_intercept
    # --------------------------

    return y


if __name__ == "__main__":
    x = np.arange(5)
    print(solution(x, 2, 4))
    print(solution(x, -1, 3))
    print(solution(x, -10, 4))
