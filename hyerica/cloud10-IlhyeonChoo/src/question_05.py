def solution(numbers):
    """
    숫자들의 리스트 numbers가 주어졌을 때, 100이상, 999이하의 숫자만 고르는 코드를 작성하세요.
    solution을 반복호출하는 재귀형태로 작성하세요.

    인자:
        - numbers: 숫자들의 리스트
    반환값:
        - 100이상, 999이하의 숫자들의 리스트

    예상출력:
        [132, 134]
        [415, 561, 423]
        []
    """

    # ----- your code here -----
    if not numbers:
        return []
    filtered_numbers = solution(numbers[1:])
    if 100 <= numbers[0] <= 999:
        return [numbers[0]] + filtered_numbers
    return filtered_numbers
    
    # --------------------------
    

if __name__ == "__main__":
    print(solution([30, 132, 41, 1561, 134]))
    print(solution([415, 561, 423, 1156]))
    print(solution([6, 14, 62, 1]))
