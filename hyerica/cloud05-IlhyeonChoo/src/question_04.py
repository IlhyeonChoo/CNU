def count_positive(numbers):
    """
    **문제**
    정수로 이루어진 numbers 라는 이름의 리스트가 주어졌을 때, 저장된 원소 중 양의 정수(> 0)의 개수를 구하세요.
    numbers는 정수로 이루어진 리스트로 주어집니다. (예: my_list = [31, -241, 3214, -312, 243])

    본 파일을 실행했을 때의 예상출력: 
        3
    """
    count = 0

    # ===== Your code here =====
    for number in numbers:
        if number > 0:
            count += 1

    # ==========================

    return count


if __name__ == "__main__":
    my_list = [31, -241, 3214, -312, 243]
    print(count_positive(my_list))