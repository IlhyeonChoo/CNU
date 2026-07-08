def solution(list_of_string):
    """
    문자열의 리스트 list_of_string이 주어졌을 때, 리스트 내 각 문자열을 모두 대문자로 만드는 코드를 작성하세요
    (즉, list(map(lambda s: s.upper(), list_of_string)) 와 같은 역할을 하는 코드 작성)
    solution을 반복호출하는 재귀형태로 작성하세요.

    인자:
        - list_of_string: 문자열의 리스트
    반환값:
        - 원소가 모두 대문자화된 문자열의 리스트

    예상출력:
        ['A', 'B']
        ['AAA', 'BBBBB']
        ['THIS', 'IS', 'A', 'SIMPLE', 'SENTENCE']
    """

    # ----- your code here -----
    if not list_of_string:
        return []
    return [list_of_string[0].upper()] + solution(list_of_string[1:])
    
    # --------------------------


if __name__ == "__main__":
    print(solution(["a", "b"]))
    print(solution(["aaa", "bbbbb"]))
    print(solution(["this", "is", "a", "simple", "sentence"]))
