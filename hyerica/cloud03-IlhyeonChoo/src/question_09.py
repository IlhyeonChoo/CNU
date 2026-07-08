def solution(string):
    """
    **문제**
    - 주어진 문장(string)에서 공백을 제외한 모든 알파벳의 빈도수 합을 계산하세요.
    - 문장에 존재하는 모든 알파벳의 빈도수를 세고 공백을 제외한 빈도수의 합을 반환합니다.
    - 예를들어, 문장에서 'a'가 5번, 'b'가 3번, 'c'가 2번 등으로 나타난다면, 5 + 3 + 2 = 10을 반환합니다.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 결과: 36

    **힌트**
    - 반복문을 사용하여 각 알파벳을 key로 하고 등장하는 빈도수를 value로 하는 딕셔너리 만들기
    - 반복문, 조건문을 조합하여 공백을 제외한 알파벳 빈도수의 합 계산하기

    **주의**
    - 반환되는 형태가 반드시 int 자료형 이어야 합니다.
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    length = len(string)
    for char in string:
        if char == ' ':
            length -= 1
    # ==========================

    return length

if __name__ == "__main__":
    string = 'The quick brown fox jumps over the lazy dog.'
    my_answer = solution(string)
    print(my_answer)