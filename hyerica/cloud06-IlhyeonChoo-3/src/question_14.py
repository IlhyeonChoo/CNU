def solution(words):
    """
    **문제**
    단어들이 담긴 리스트(words)가 주어졌을 때,
    각 단어를 key로, 해당 단어의 길이를 value로 하는 딕셔너리를 생성하여 반환하세요.
    이 문제는 딕셔너리 컴프리헨션(dictionary comprehension)을 활용하는 연습입니다.

    **예시**
    입력: ["apple", "banana", "kiwi"]
    출력: {'apple': 5, 'banana': 6, 'kiwi': 4}

    **주의**
    - 함수 내부에서는 외부 전역 변수(my_list 등)를 직접 사용하지 마세요.
    - 반드시 딕셔너리 컴프리헨션을 사용하여 작성하세요.
    """
    # ===== Your code here =====
    dictionary = {word: len(word) for word in words}

    # ==========================
    
    
    return dictionary
    
if __name__ == "__main__":
    my_list = ["apple", "banana", "kiwi"]
    answer = solution(my_list)
    print(answer)
