def solution(n, m):
    """
    **문제**
    - 두 숫자 (n, m) 사이의 모든 숫자를 담은 리스트를 반환하는 코드를 작성하세요. (n과 m은 포함되지 않음!)
    - 단, 두 숫자가 같은 경우 빈 리스트를 반환합니다. 
    - n은 항상 m 보다 작은 수 입니다. (n < m)
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 결과: [24, 25, 26, 27, 28, 29, 30, 31, 32]
    """
    # ===== Your code here =====
    my_answer = []

    for number in range(n + 1, m):
        my_answer.append(number)

    # ==========================

    return my_answer

if __name__ == "__main__":
    n, m = 23, 33
    my_answer = solution(n, m)
    print(my_answer)