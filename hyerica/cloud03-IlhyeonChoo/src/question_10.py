def solution(numbers):
    """
    **문제**
    - 주어진 리스트(numbers)에서 리스트의 길이가 8이고, 리스트의 5번째 숫자가 3개인 경우 True를 반환하고, 그 외의 경우 False를 반환하는 함수를 작성하세요.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 결과: True

    **힌트**
    - 리스트의 길이, 5번째 숫자, 카운트를 담는 변수를 활용해보세요.
    - 반복문, 조건문을 조합하여 리스트의 길이가 8이고, 5번째 요소가 3개인지 확인

    **주의**
    - 반환되는 형태가 반드시 bool 자료형 이어야 합니다.
    - 리스트의 길이가 8이 아니거나, 5번째 요소가 3개가 아닌 경우 False를 반환해야 합니다.
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    number_5 = numbers[4]
    check_num = 0
    for number in numbers:
        if number == number_5:
            check_num += 1

    result = check_num == 3
    # ==========================

    return result

if __name__ == "__main__":
    # numbers 리스트 내부의 원소 개수가 8개 이고, 5번째 숫자(5)가 3개이므로 True를 반환합니다.
    numbers = [19, 19, 15, 5, 5, 5, 1, 2]
    my_answer = solution(numbers)
    print(my_answer)