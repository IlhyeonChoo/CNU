def solution(numbers, descending=False):
    """
    숫자들의 리스트 numbers가 주어졌을 때, 이 숫자들을 정렬하는 코드를 작성하세요(sorted 함수 작성).
    이때, sort, sorted 함수는 사용하지 말고, 재귀함수로 구현하세요.
    또, 두 번째 인자인 descending 여부에 따라, descending=True 일 경우, 큰 수가 앞에 오도록, descending=False일 경우, 작은 수가 앞에오도록 정렬하세요.

    힌트:
        - solution 함수의 반환값의 데이터 형식은 list가 되면 됩니다(다른 방식으로 해도 됩니다).
        - 종료조건에서는 빈 리스트를 반환하거나, 원소가 하나만 있는 리스트를 반환하면 됩니다.
        - 종료조건이 아닐 때는, numbers에서 제일 작은 수(또는 제일 큰 수)를 뽑아서 [뽑은 수] + solution(...)를 반환해주시면 됩니다.
        - solution을 반복 호출하실때, numbers에서 뽑힌 수는 제거할 필요가 있습니다.

    인자:
        - numbers: 숫자들의 리스트
        - descending: True이면 내림차순 정렬

    예상출력:
        [1, 3, 3, 12, 34]
        [34, 12, 3, 3, 1]
    """

    # ----- your code here -----
    if not numbers:
        return []
    target = max(numbers) if descending else min(numbers)
    remaining = numbers.copy()
    remaining.remove(target)
    return [target] + solution(remaining, descending=descending)
    
    # --------------------------


if __name__ == "__main__":
    print(solution([3, 1, 34, 12, 3]))
    print(solution([3, 1, 34, 12, 3], descending=True))
