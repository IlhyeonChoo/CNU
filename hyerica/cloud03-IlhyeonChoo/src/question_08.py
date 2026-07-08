def solution(words, n):
    """
    **문제**
    - 주어진 리스트(words)에서 단어의 길이가 n 보다 긴 단어를 찾아 리스트로 반환하는 함수를 작성하세요.
    - 예를 들어, n=3이고 단어가 'brown' 일때 brown의 알파벳의 길이가 4이므로 결과에 포함됩니다.
    - 하지만 n=3이고 단어가 'fox' 일때 fox의 알파벳의 길이가 3이므로 포함되지 않습니다.
    - n은 0보다 큰 정수이고 여기서는 3으로 가정합니다.
    - 아래 처럼 출력 값이 나오면 성공입니다.
    - 출력: ['quick', 'brown']

    **힌트**
    - 정답을 담을 새로운 리스트 만들기
    - 단어의 길이가 n보다 긴지 확인하기
    - 반복문, 조건문을 조합하여 문제를 풀어보세요.

    **주의**
    - 반환되는 형태가 반드시 리스트여야 합니다.
    - 리스트 내부의 단어는 반드시 str 자료형 이어야 합니다.
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    
    # ==========================
    
    return result

if __name__ == "__main__":
    n = 3
    words = ['The', 'quick', 'brown', 'fox', '.']
    my_answer = solution(words, n)
    print(my_answer)