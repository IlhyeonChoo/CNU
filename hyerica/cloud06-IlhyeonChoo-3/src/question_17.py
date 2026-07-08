def solution(sentence):
    """
    **문제**
    콤마(,)와 콜론(:)으로 구성된 문자열(sentence)이 주어졌을 때,
    각 콜론(:) 앞의 단어를 key로, 뒤의 단어를 value로 하여 딕셔너리를 생성하는 코드를 작성하세요.
    각 쌍은 쉼표(,)로 구분되며, key와 value는 문자열입니다.

    **예시**
    입력: "name:John,age:30,job:dev"
    출력: {'name': 'John', 'age': '30', 'job': 'dev'}

    **힌트**
    - 먼저 문자열을 쉼표(,) 기준으로 나눈 후, 각 항목을 콜론(:) 기준으로 나눠서 처리하세요.
    - 딕셔너리에 key-value를 추가하세요.

    **주의**
    - 함수 내부에서는 외부 전역 변수(text 등)를 직접 사용하지 마세요.
    - key와 value는 모두 문자열로 처리하며, 숫자로 변환하지 않습니다.
    - 모든 항목은 콜론(:)을 정확히 1개 포함한다고 가정합니다.
    """
    # ===== Your code here =====
    dictionary = {}
    for item in sentence.split(","):
        key, value = item.split(":")
        dictionary[key] = value

    # ==========================
    
    return dictionary
    
if __name__ == "__main__":
    text = "name:John,age:30,job:dev"
    answer = solution(text)
    print(answer)
