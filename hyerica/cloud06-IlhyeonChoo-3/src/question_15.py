def solution(alphabets):
    """
    **문제**
    알파벳 소문자로 이루어진 리스트 alphabets가 주어졌을 때, 
    각 알파벳을 key로 하고 해당 알파벳의 대문자를 value로 가지는 딕셔너리를 생성하여 반환하세요.
    이 문제는 딕셔너리 컴프리헨션(dictionary comprehension)을 활용하는 연습입니다.

    **예시**
    입력: ['a', 'b', 'c', 'd']
    출력: {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}

    **주의**
    - 반드시 딕셔너리 컴프리헨션을 사용하여 문제를 해결하세요.
    - 함수 내부에서는 외부 전역 변수(my_list 등)를 직접 사용하지 마세요.
    """
    # ===== Your code here =====
    dictionary = {alphabet: alphabet.upper() for alphabet in alphabets}

    # ==========================
    
    
    return dictionary
    
if __name__ == "__main__":
    my_chars = ['a', 'b', 'c', 'd']
    answer = solution(my_chars)
    print(answer)
