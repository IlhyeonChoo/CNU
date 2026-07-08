def solution(start, end, result=0):
    """
    두 자연수 start, end가 주어졌을 때, start부터 end까지 모든 자연수들의 합을 구하는 코드를 작성하세요.
    이때, 반복문을 사용하지 말고 재귀함수로 작성하는데, 이번에는 이 함수의 return 문을 다음과 같은 형식으로 구현하세요.
    return solution(...)
    즉, return문에는 어떠한 더하기 연산도 포함되지 않고, solution 호출 결과만 반환하도록 해야 합니다.
    더하기 중간 결과는 solution의 세 번째 인자인 result에 저장하세요.
    이를 꼬리재귀(tail recursion)라고 합니다.

    예를들어,
    solution(1, 4)를 호출하게 되면, 1 + solution(2, 4)을 반환하는 대신, solution(2, 4, 1)를 반환하고,
    solution(2, 4, 1)는 solution(3, 4, 3)을 반환하고,
    solution(3, 4, 3)은 solution(4, 4, 6)을 반환하고,
    solution(4, 4, 6)은 10을 반환하게 하면 됩니다.
    
    이때, start, end 모두 더하기할 자연수로 포함합니다.
    예: start = 1, end = 5 일 경우, 최종 결과는
    1 + 2 + 3 + 4 + 5 = 15 가 되어야 합니다.

    인자:
        - start: 덧셈을 시작할 자연수
        - end: 덧셈을 완료할 자연수
        - result: start~end 까지 더하기하는 과정의 중간결과물
    반환값:
        - solution(start, end, 중간결과물) 형태

    예상결과:
        55
        65
        462
    """
    
    # ----- your code here -----
    if start > end:
        return result
    return solution(start + 1, end, result + start)

    # --------------------------


if __name__ == "__main__":
    print(solution(1, 10))
    print(solution(2, 11))
    print(solution(33, 44))
