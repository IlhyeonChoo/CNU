import sys, os
sys.path.append(os.path.dirname(__file__))

# ----- Your code here -----
# question_01을 import 하세요.
from question_01 import calculate_mean, calculate_std


def standardize(*numbers):
    """
    숫자들이 주어졌을 때, 숫자들을 표준정규화하는 함수를 작성하세요.
    표준정규화는 (X - mu) / std 를 의미합니다. X 자리에 numbers의 숫자 하나하나가 들어가면 되고, mu와 std는 numbers의 평균과 표준편차입니다.

    이때, 평균과 표준편차는 이미 question_01.py에서 구현했었습니다(calculate_mean, calculate_std).
    작성해둔 두 함수를 호출하여 평균과 표준편차를 구하세요.
    평균과 표준편차를 이용하여 numbers의 각 숫자들을 표준정규화할때는 map 함수를 이용하여 구현하세요.
    calculate_mean, calculate_std를 호출할때, 인자로는 *numbers 로 넣어주세요(numbers앞에 별 붙여주세요. list unpacking)

    인자:
    - numbers: 숫자들

    반환값:
    - numbers_standardized: 표준정규화된 숫자들
    """
    
    # question_01의 calculate_mean, calculate_std 활용
    mean = calculate_mean(*numbers)
    std = calculate_std(*numbers)

    # map 함수 활용
    numbers_standardized = list(map(lambda number: (number - mean) / std, numbers))
    
    return numbers_standardized
# --------------------------


if __name__ == "__main__":
    """
    예상출력: (매우작은 소수점오차는 발생할 수 있음)
        [1.3989019475666278, -0.6482716342381933, -1.1941845893861458, 0.44355427605771125]
        [-0.23827606734886683, -0.35419415416723443, -0.3851056439854658, -0.2923711745307717, -0.910600970895399, 2.1805480109277373]
        [0.8736509697457411, -0.6057144078033699, -0.7326985603826928, -1.0374605265730676, 1.5022225250133892]
    """

    print(standardize(100, 85, 81, 93))
    print(standardize(100, 85, 81, 93, 13, 413))
    print(standardize(314, 81, 61, 13, 413))
