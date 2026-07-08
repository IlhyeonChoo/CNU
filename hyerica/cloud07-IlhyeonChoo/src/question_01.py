# ----- Your code here -----
def calculate_mean(*numbers):
    """
    숫자들을 입력받아 숫자들의 평균을 계산하는 함수를 작성하세요.
    이때, 함수의 signature는 아래 적혀있는 "인자", "반환값"에 맞춰서 작성하세요..

    단, 숫자들의 리스트를 입력받게 하지말고, 가변인자로 입력받게 하세요.
    예를들어,
        calculate_mean(10) -> 10
        calculate_mean(10, 20) -> 15
        calculate_mean(10, 15, 20) -> 15
    처럼 함수를 호출할 수 있어야 합니다.

    인자:
    - numbers: 숫자입력들

    반환값:
    - mean: numbers의 평균값
    """

    mean = sum(numbers) / len(numbers)
    return mean


def calculate_std(*numbers):
    """
    숫자들을 입력받아 숫자들의 표준편차를 계산하는 함수를 작성하세요. 표준편차는 분산의 루트값입니다.
    분산을 계산할때, 편차제곱을 평균내주어야 하는데, 편차제곱의 합산을 숫자들의 개수로 나눠주세요("숫자개수 - 1"로 나눠주지 마세요).
    a의 루트값은 "a ** 0.5"로 구할 수 있습니다.
    이때, 함수의 signature는 아래 적혀있는 "인자", "반환값"에 맞춰서 작성하세요.

    단, 숫자들의 리스트를 입력받게 하지말고, 가변인자로 입력받게 하세요.
    예를들어,
        calculate_std(10, 20) -> 5.0
        calculate_std(10, 15, 20) -> 4.08248290463863
    처럼 함수를 호출할 수 있어야 합니다.

    인자:
    - mean: 평균값
    - numbers: 숫자입력들

    반환값:
    - std: numbers의 표준편차
    """

    # list unpacking: 
    # numbers -> [100, 93] >>>>> *numbers -> 100, 93
    mean = calculate_mean(*numbers) 
    variance = sum((number - mean) ** 2 for number in numbers) / len(numbers)
    std = variance ** 0.5
    return std
# --------------------------
    

if __name__ == "__main__":
    """
    예상출력: (매우작은 소수점 오차는 발생할 수 있음)
        Mean: 89.75, Std: 7.327175444876422
        Mean: 130.83333333333334, Std: 129.40172160970482
        Mean: 176.4, Std: 157.49996825396505
    """

    mean = calculate_mean(100, 85, 81, 93)
    std = calculate_std(100, 85, 81, 93)
    print(f"Mean: {mean}, Std: {std}")

    mean = calculate_mean(100, 85, 81, 93, 13, 413)
    std = calculate_std(100, 85, 81, 93, 13, 413)
    print(f"Mean: {mean}, Std: {std}")

    mean = calculate_mean(314, 81, 61, 13, 413)
    std = calculate_std(314, 81, 61, 13, 413)
    print(f"Mean: {mean}, Std: {std}")
