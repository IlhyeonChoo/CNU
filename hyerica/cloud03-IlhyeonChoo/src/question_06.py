def solution(numbers):
    """
    **문제**
    - 주어진 리스트(numbers)에서 중복된 숫자는 제거하고, 홀수만 남긴 리스트를 반환하는 코드를 작성하세요.
    - 단, 짝수만 존재하는 경우 빈 리스트를 반환합니다.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 결과: [1, 3, 43]

    **힌트**
    - 정답을 담을 새로운 리스트 만들기
    - 홀수가 아니라면 건너뛰기
    - 이미 추가된 값이 아니라면 리스트에 추가하기
    - 반복문, 조건문을 조합하여 문제를 풀어보세요.

    **주의**
    - 반환되는 형태가 반드시 리스트여야 합니다.
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    even_list = []
    for number in numbers:
        if number % 2 == 1:
            check_bool = False
            for check_num in even_list:
                if check_num == number:
                    check_bool = True
            if check_bool:
                check_bool = False
                continue
            else:
                even_list.append(number)
    # ==========================

    return even_list

if __name__ == "__main__":
    numbers = [1, 3, 4, 10, 4, 1, 43]
    my_answer = solution(numbers)
    print(my_answer)