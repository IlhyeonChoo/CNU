def solution(sentence):
    """
    **문제**
    주어진 문장(sentence)을 공백(띄어쓰기)을 기준으로 나누어, 각 단어를 리스트로 반환하는 코드를 작성하세요.
    단, 문자열의 내장 메서드인 split()은 사용하지 마세요.

    **예시**
    입력: "the quick brown fox"
    출력: ['the', 'quick', 'brown', 'fox']

    **힌트**
    - 문장을 문자 단위로 하나씩 순회하며 공백이 아닌 문자는 임시 변수(word)에 추가하세요.
    - 공백이 나오면 지금까지 만든 단어를 리스트에 저장하고, word를 초기화하세요.
    - 마지막 단어도 꼭 리스트에 추가해 주세요.

    **주의**
    - 반드시 split()을 사용하지 않고 구현해야 합니다.
    - 함수 내부에서는 외부 전역 변수(text 등)를 직접 사용하지 마세요.
    - 문장 내 단어는 공백 하나로만 구분된다고 가정합니다.
    """
    # ===== Your code here =====
    words = []
    word = ""
    for char in sentence:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)

    # ==========================
    

    return words
    
if __name__ == "__main__":
    text = "the quick brown fox"
    answer = solution(text)
    print(answer)
