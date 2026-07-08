import numpy as np


def solution(matrix, crop):
    """
    2차원(m x m) 정방행렬이 주어졌을 떄, 행렬의 가장자리의 몇 개의 층을 제거한 행렬을 반환하는 코드를 작성하세요.
    이때, 가장자리의 몇 층을 제거할지는 crop 인자로 주어집니다.
    예를들어, 
    1. crop=2이고, 5x5 행렬이 다음과 같이 주어졌을 경우,
        [[1, 2, 3, 2, 1],
         [1, 3, 5, 3, 1],
         [1, 4, 7, 4, 1],
         [1, 3, 5, 3, 1],
         [1, 2, 3, 2, 1]]
       반환값은은 다음과 같아야 합니다. (상하좌우 2줄씩 제거)
        [[7]]
    2. crop=1이고, 다음과 같이 4x4 행렬의 경우,
        [[1, 2, 2, 1],
         [2, 4, 4, 2],
         [4, 8, 8, 4],
         [8, 16, 16, 8]]
       다음과 같은 행렬이 구해져야 합니다. (상하좌우 1줄씩 제거)
        [[4, 4],
         [8, 8]]

    행렬 matrix는 항상 2x2 정방행렬이라고 가정하며, 행/열의 개수는 고정되지 않으나, 행과 열의 개수는 같다고 가정합니다.

    인자:
        - matrix: m x m 정방행렬
    반환값:
        - matrix의 정중앙 부분행렬. ((m + 1)/2, (m + 1)/2) 차원

    예상출력:
        [[16 17 18]
        [23 24 25]
        [30 31 32]]
        [[7]]
        [[4 4]
        [8 8]]
    """
    
    # ----- your code here -----
    if crop == 0:
        return matrix

    return matrix[crop:-crop, crop:-crop]

    # --------------------------


if __name__ == "__main__":
    np.random.seed(13)
    
    matrix1 = np.arange(49).reshape(7, 7)
    ret = solution(matrix1, 2)
    print(ret)
    
    matrix2 = np.array([[3, 5, 3],
                        [4, 7, 4],
                        [3, 5, 3]])
    ret = solution(matrix2, 1)
    print(ret)
    
    matrix3 = np.array([[1, 2, 2, 1],
                        [2, 4, 4, 2],
                        [4, 8, 8, 4],
                        [8, 16, 16, 8]])
    ret = solution(matrix3, 1)
    print(ret)
