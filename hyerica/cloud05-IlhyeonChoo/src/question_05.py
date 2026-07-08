def solution(numbers):
    """
    **문제**
    - 리스트에서 가장 많이 등장하는 수(최빈값)를 찾는 코드를 작성하세요.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 결과: 4
    """
    # ===== Your code here =====
    mode_value = numbers[0]
    max_count = 0

    for number in numbers:
        current_count = numbers.count(number)
        if current_count > max_count:
            max_count = current_count
            mode_value = number

    # ==========================

    return mode_value

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 4, 10, 4, 1, 9, 9, 43]
    my_answer = solution(numbers)
    print(my_answer)