import os
import numpy as np
import matplotlib.pyplot as plt


def solution(a, b, steps):
    """
    이차함수 y = ax^2 + b에서, a와 b가 각각 주어졌을 때, x와 y를 다음과 같이 생성하고 반환하세요.
    x: 0부터 10까지의 숫자로 이루어진 넘파이 배열인데, 그 원소의 개수는 steps가 되어야 합니다. 이때, 각 원소는 0에서 10 사이를 (step-1) 등분하도록 해야 합니다.
    예를들어, steps=10일 경우, x는 다음과 같이야 합니다.
    array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])

    for문 사용하지마세요.
    
    y는 이차함수의 값(x에 대응하는 치역값)이어야 합니다.

    인자:
        - a: 실수 하나. 이차함수의 기울기
        - b: 실수 하나. 이차함수의 y 절편
        - steps: 자연수 하나. x를 구하기 위한 정수의 개수

    반환값:
        - x: 0부터 10까 사이를 (steps-1) 등분한 steps 개의 실수로 이루어진 넘파이 배열
        - y: x에 대응하는 이차함수값

    예상출력
        파일 실행 후, resources/ 폴더 내에 q4_steps3.jpg, q4_steps9.jpg, q4_steps30.jpg 파일을 확인해보세요.
        세 파일에 출력된 그래프가 q4_steps3_truth.jpg, q4_steps9_truth.jpg, q4_steps30_truth.jpg 와 같으면 됩니다.
    """

    # ----- your code here -----
    x = np.linspace(0, 10, steps)
    y = a * x**2 + b
    return x, y

    # --------------------------


if __name__ == "__main__":
    x1, y1 = solution(2, 2, 3)
    x2, y2 = solution(2, 2, 9)
    x3, y3 = solution(2, 2, 30)

    root_dir = os.path.dirname(os.path.dirname(__file__))

    plt.figure()
    plt.plot(x1, y1, c="blue", marker="o")
    plt.savefig(os.path.join(root_dir, "resources", "q4_steps3.jpg"))

    plt.figure()
    plt.plot(x2, y2, c="blue", marker="^")
    plt.savefig(os.path.join(root_dir, "resources", "q4_steps9.jpg"))

    plt.figure()
    plt.plot(x3, y3, c="blue", marker="*")
    plt.savefig(os.path.join(root_dir, "resources", "q4_steps30.jpg"))
