import numpy as np


def solution(M):
    """
    이번에는, 행렬이 아닌, 임의의 랭크를 가진 고차원 텐서의 -2번째 축(뒤에서 두 번째 축)에서, i번째 차원에 i를 더해주는 코드를 작성하세요.
    예를들어, M이 (5, 3, 4) 모양일 경우,
    M[:, 0, :] 에는 0이 더해저야 하고, M[:, 1, :]에는 1이 더해져야 하고, M[:, 2, :]에는 2가 더해져야 합니다.

    반복문 및 map 연산은 사용하지 말고, 두 넘파이 배열을 더하는 형태로 코드를 구현하세요.

    인자:
        - M: 임의 모양의 텐서(rank 2 이상)
        - axis: M 텐서에서의 축 인덱스(축 번호)

    반환값:
        - result: M 텐서의 axis 번째 축에서 i 번째 차원에 i가 더해진 텐서

    예상출력:
        [[[[0. 0.]
        [1. 1.]
        [2. 2.]]

        [[0. 0.]
        [1. 1.]
        [2. 2.]]

        [[0. 0.]
        [1. 1.]
        [2. 2.]]]


        [[[0. 0.]
        [1. 1.]
        [2. 2.]]

        [[0. 0.]
        [1. 1.]
        [2. 2.]]

        [[0. 0.]
        [1. 1.]
        [2. 2.]]]]
        ---
        [[[0. 0.]
        [1. 1.]
        [2. 2.]]

        [[0. 0.]
        [1. 1.]
        [2. 2.]]]
        ---
        [[0. 0. 0. 0.]
        [1. 1. 1. 1.]
        [2. 2. 2. 2.]]
    """

    # ----- Your code here -----
    
    shape = [1] * M.ndim
    shape[-2] = M.shape[-2]
    offsets = np.arange(M.shape[-2]).reshape(shape)
    result = M + offsets
    # --------------------------
    return result


if __name__ == "__main__":
    A = np.zeros((2, 3, 3, 2))
    res = solution(A)
    print(res)
    print("---")

    A = np.zeros((2, 3, 2))
    res = solution(A)
    print(res)
    print("---")

    A = np.zeros((3, 4))
    res = solution(A)
    print(res)


    
