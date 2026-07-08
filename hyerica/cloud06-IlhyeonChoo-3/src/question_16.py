def solution(sentence):
    """
    **문제**
    주어진 문장(sentence)에서 불용어(stopwords)를 제외한 단어들의 빈도를 계산하는 코드를 작성하세요.
    불용어는 다음과 같습니다: {"the", "over"}
    모든 단어는 소문자로 처리하며, 동일한 단어가 여러 번 등장할 경우 빈도수로 계산해야 합니다.

    **예시**
    입력: "the quick brown fox jumps over the lazy dog the quick fox"
    출력: {'quick': 2, 'brown': 1, 'fox': 2, 'jumps': 1, 'lazy': 1, 'dog': 1}

    **힌트**
    - 문자열은 .lower().split()을 통해 단어로 나눌 수 있습니다.
    - 리스트 컴프리헨션을 통해 불용어를 제거하세요.
    - 불용어가 제거된 단어들의 빈도수를 계산하세요.

    **주의**
    - 함수 내부에서는 외부 전역 변수(my_string 등)를 직접 사용하지 마세요.
    """
    stopwords = {"the", "over"} # 불용어를 제외하고 단어들의 빈도를 계산하세요.

    # ===== Your code here =====
    word_count = {}
    words = [word for word in sentence.lower().split() if word not in stopwords]
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # ==========================
    
    return word_count
    
if __name__ == "__main__":
    my_string =  "the quick brown fox jumps over the lazy dog the quick fox"
    answer = solution(my_string)
    print(answer)
