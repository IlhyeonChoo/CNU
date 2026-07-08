def solution(string):
    """
    **문제**
    - 주어진 문장(string)에서 단어의 순서를 거꾸로 바꾸되, 각 단어 내부의 알파벳 순서는 유지하세요.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 입력: 'Artificial Intelligence is amazing'
    - 결과: 'amazing is Intelligence Artificial'

    **힌트**
    - 문장을 단어 단위로 쪼갭니다.
    - 단어의 순서를 거꾸로 뒤집습니다.
    - 단어를 다시 하나의 문장으로 합칩니다.

    **주의**
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    word_list = string.split()
    result_list = []
    for word in word_list:
        result_list.insert(0, word)

    result = " ".join(result_list)
    # ==========================
    
    return result

if __name__ == "__main__":
    string = "Artificial Intelligence is amazing"
    my_answer = solution(string)
    print(my_answer)