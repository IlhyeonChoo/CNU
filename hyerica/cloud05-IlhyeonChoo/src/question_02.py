def solution(numbers):
    """
    **문제**
    - 여러 자료형이 담긴 리스트에서 모든 수의 합을 계산하는 코드를 작성하세요.
    - 아래와 같이 결과값이 나오면 성공입니다.
    - 결과: 70.14
    """
    # ===== Your code here =====
    sum = 0

    for number in numbers:
        if isinstance(number, str):
            if "." in number:
                sum += float(number)
            else:
                sum += int(number)
        else:
            sum += number

    # ==========================

    return sum

if __name__ == "__main__":
    numbers = [1, '3', True, 4, '10', 4, False, '1', 43, 3.14]
    my_answer = solution(numbers)
    print(my_answer)