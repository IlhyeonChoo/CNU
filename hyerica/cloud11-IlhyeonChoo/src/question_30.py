import os
import numpy as np
import matplotlib.pyplot as plt


def solution(X, mean, std):
    """
    x, y 두 축으로 구성된 데이터포인트 n개로 구성된 (n, 2) 모양의 데이터셋이 주어지고, 
    두 개의 평균/표준편차 쌍이 주어졌을 때, n개의 데이터셋의 절반(0 ~ n/2)은 첫 번째 표준편차 쌍으로 비정규화 하고, 나머지 절만(n/2 ~ n)은 두 번째 표준편차 쌍으로 비정규화를 수행하시오.

    이때, 한 개의 평균과 한 개의 표준편차는 각각 (1, 2) 모양입니다(x, y 좌표 평균이 1개, x, y 좌표 표준편차가 1개).
    인자로 주어지는 mean은 두 개의 평균이므로, (2, 2) 모양입니다(한 row가 하나의 평균(x, y 좌표 평균)). 표준편차도 마찬가지입니다.
    예:
        mean = [[mean_x1, mean_y1],
                [mean_x2, mean_y2]]

    데이터 비정규화는 데이터를 표준정규화 한 것에 다시 표준편차를 곱하고 평균을 더해주는 방식으로 구현하세요. 
    특정 평균과 표준편차로 비정규화를 거치면, 해당 데이터의 평균과 표준편차는 주어진 평균과 표준편차가 됩니다.

    예를들어, 원본 데이터를 X라 하고, 표준정규화된 데이터를 X_std, 비정규화된 데이터를 X_denorm 이라고 헀을 때, X_denorm을 구하는 과정은 다음과 같습니다.
    1. mu, sigma <- mean(X), std(X)         # 평균벡터, 표준편차 벡터 계산. 각각 (2,) 모양
    2. X_std <- (X - mu) / sigma            # 표준정규화 (원본 데이터의 평균, 표준편차 이용)
    3. X_denorm <- X_std * std + mean       # 비정규화   (원본이 아닌, 다른 평균과 표준편차 이용)

    인자:
        - X: x, y 두 축 좌표값으로 구성된 데이터포인트 n개로 이루어진 (n, 2) 모양의 데이터셋
        - mean: 두 개의 (x, y) 평균으로 이루어진 (2, 2) 모양의 넘파이 배열. 하나의 row가 하나의 (x, y) 평균임
        - std: 두 개의 (x, y) 표준편차로 이루어진 (2, 2) 모양의 넘파이 배열. 하나의 row가 하나의 (x, y) 표준편차임

    반환값:
        - 절반씩 서로다른 mean, std로 비정규화한 데이터

    예상출력:
        resources/ 아래 생성된 q10_test1.png, q10_test2.png, q10_test3.png 이 *_truth.png 와 거의 같게 찍히면 성공입니다.
    """

    # ----- Your code here -----
    
    # 1. 데이터의 절반씩 정규화하기
    half = X.shape[0] // 2
    X1 = X[:half]
    X2 = X[half:]

    X1_std = (X1 - np.mean(X1, axis=0)) / np.std(X1, axis=0)
    X2_std = (X2 - np.mean(X2, axis=0)) / np.std(X2, axis=0)

    # 2. 절반씩 비정규화하기
    Y1 = X1_std * std[0] + mean[0]
    Y2 = X2_std * std[1] + mean[1]

    return np.concatenate([Y1, Y2], axis=0)

    # --------------------------


if __name__ == "__main__":
    np.random.seed(13)
    X = np.random.randn(100, 2)
    
    mean = np.array([[1, 1], [5, 5]])
    std = np.array([[1, 1], [1.5, 1.5]])
    Y = solution(X, mean, std)
    
    plt.figure()
    plt.scatter(Y[:Y.shape[0]//2, 0], Y[:Y.shape[0]//2, 1], c="blue")
    plt.scatter(Y[Y.shape[0]//2:, 0], Y[Y.shape[0]//2:, 1], c="orange")
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "q10_test1.png"))
    
    X = np.random.randn(200, 2)
    mean = np.array([[-1, -0.5], [3, 3.5]])
    std = np.array([[0.5, 1.5], [2, 1]])
    Y = solution(X, mean, std)
    
    plt.figure()
    plt.scatter(Y[:Y.shape[0]//2, 0], Y[:Y.shape[0]//2, 1], c="blue")
    plt.scatter(Y[Y.shape[0]//2:, 0], Y[Y.shape[0]//2:, 1], c="orange")
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "q10_test2.png"))
    
    X = np.random.randn(300, 2)
    mean = np.array([[-2.3, 1.1], [0.12, -3.4]])
    std = np.array([[1.2, 0.9], [1.3, 2.3]])
    Y = solution(X, mean, std)
    
    plt.figure()
    plt.scatter(Y[:Y.shape[0]//2, 0], Y[:Y.shape[0]//2, 1], c="blue")
    plt.scatter(Y[Y.shape[0]//2:, 0], Y[Y.shape[0]//2:, 1], c="orange")
    plt.savefig(os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "q10_test3.png"))
