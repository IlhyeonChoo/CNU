def solution(start, end):
    """
    두 자연수 start, end가 주어졌을 때, start부터 end까지 모든 자연수들의 합을 구하는 코드를 작성하세요.
    이때, 반복문을 사용하지 말고 재귀함수로 작성하세요.

    이때, start, end 모두 더하기할 자연수로 포함합니다.
    예: start = 1, end = 5 일 경우, 최종 결과는
    1 + 2 + 3 + 4 + 5 = 15 가 되어야 합니다.

    재귀함수 작성할때는,
    1. 문제 분할(같은 형태의 작은 문제로 분할)
    2. 종료조건 설정
    를 고려하시면 됩니다.

    예를들어, 다음처럼, start 변수를 하나씩 증가시켜가면서 재귀함수를 구현할 수 있습니다.
    solution(1, 4)를 호출한 경우, 1 + solution(2, 4)가 반환되어야 하며,
    solution(2, 4)의 경우, 2 + solution(3, 4)가 반환,
    solution(3, 4)는 3 + solution(4, 4)를 반환
    solution(4, 4)는 4를 반환하게 하면 됩니다.
    이 방법 이외에도 다른 재귀방식으로도 구현하셔도 됩니다.

    인자:
        - start: 덧셈을 시작할 자연수
        - end: 덧셈을 완료할 자연수

    반환값:
        - start ~ end까지 모든 자연수들의 합 (재귀식)

    예상출력:
        55
        65
        462
    """
    
    # ----- your code here -----
    if start > end:
        return 0
    if start == end:
        return start
    return start + solution(start + 1, end)

    # --------------------------


if __name__ == "__main__":
    print(solution(1, 10))
    print(solution(2, 11))
    print(solution(33, 44))
