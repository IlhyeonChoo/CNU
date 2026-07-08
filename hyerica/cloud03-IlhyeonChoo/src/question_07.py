def solution(numbers):
    """
    **문제**
    - 주어진 리스트(numbers)에서 10보다 크고, 앞뒤 양끝 숫자가 모두 홀수인 숫자만 담긴 리스트를 반환하세요.
    - 아래 처럼 출력 값이 나오면 성공입니다.
    - 출력: [79, 39, 103]

    **힌트**
    - 정답을 담을 새로운 리스트 만들기
    - 10보다 큰 수 인지 확인하기
    - 10보다 크고 홀수인 숫자인지 확인하기
    - 모두 만족한다면, 숫자를 문자열로 변환하여 맨앞 맨뒤 숫자가 모두 홀수인지 확인하기
    - 반복문, 조건문을 조합하여 문제를 풀어보세요.

    **주의**
    - 반환되는 형태가 반드시 리스트여야 합니다.
    - 10은 포함되지 않습니다.
    - 리스트 내부에 숫자는 반드시 int 자료형 이어야 합니다.
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    even_list = []
    for number in numbers:
        if number > 10 and number % 2 == 1:
            num = number
            while num < 10:
                num /= 10
            if num % 2 == 1:
                even_list.append(num)

    
    # ==========================
    
    return even_list

if __name__ == "__main__":
    numbers = [1, 3, 79, 10, 4, 1, 39, 62 ,103, 246]
    my_answer = solution(numbers)
    print(my_answer)