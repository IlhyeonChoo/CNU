import numpy as np


def solution():
    """
    다음과 같이 세 개의 넘파이 배열을 생성하세요.
    1. 0으로만 구성된 (2, 3) 모양의 넘파이 배열
    2. 1로만 구성된 (2, 3, 2) 모양의 넘파이 배열
    3. standard gaussian 분포에서 샘플링된 원소로만 구성된 (2, 4, 4) 모양의 넘파이 배열

    인자:
        - 없음
    반환값:
        - zero_tensor: 0으로만 구성된 (2, 3) 모양의 넘파이 배열
        - one_tensor: 1로만 구성된 (2, 3, 2) 모양의 넘파이 배열
        - standard_gaussian_tensor: standard gaussian 분포에서 샘플링된 원소로만 구성된 (2, 4, 4) 모양의 넘파이 배열

    예상출력:
        zero_tensor:
        [[0. 0. 0.]
        [0. 0. 0.]]
        one_tensor:
        [[[1. 1.]
        [1. 1.]
        [1. 1.]]

        [[1. 1.]
        [1. 1.]
        [1. 1.]]]
        standard_gaussian_tensor:
        [[[-0.71239066  0.75376638 -0.04450308  0.45181234]
        [ 1.34510171  0.53233789  1.3501879   0.86121137]
        [ 1.47868574 -1.04537713 -0.78898902 -1.26160595]
        [ 0.56284679 -0.24332625  0.9137407   0.31735092]]

        [[ 0.12730328  2.15038297  0.60628866 -0.02677165]
        [-0.98416078  1.19070527  0.95283061 -1.08718159]
        [-0.14521133  0.23785784 -1.63909341 -0.27813452]
        [ 1.39923842 -1.61510796  0.49087183  1.89274222]]]
    """

    # ----- your code here -----
    zero_tensor = np.zeros((2, 3))
    one_tensor = np.ones((2, 3, 2))
    standard_gaussian_tensor = np.random.randn(2, 4, 4)
    # --------------------------

    return zero_tensor, one_tensor, standard_gaussian_tensor


if __name__ == "__main__":
    np.random.seed(13)
    zero_tensor, one_tensor, standard_gaussian_tensor = solution()
    print("zero_tensor:")
    print(zero_tensor)
    print("one_tensor:")
    print(one_tensor)
    print("standard_gaussian_tensor:")
    print(standard_gaussian_tensor)
