def solution(dict1, dict2):
    """
    **문제**
    두 개의 딕셔너리(dict1, dict2)가 주어졌을 때, 
    dict2의 키-값 쌍을 dict1에 병합하는 코드를 작성하세요.

    - 만약 dict2의 키가 dict1에 없다면 해당 키-값 쌍을 추가합니다.
    - 만약 키가 이미 dict1에 존재한다면, dict2의 값을 dict1의 기존 값에 더합니다.

    **예시**
    입력: {'a': 1, 'b': 2}, {'b': 3, 'c': 4, 'd': 5}
    출력: {'a': 1, 'b': 5, 'c': 4, 'd': 5}

    **힌트**
    - 딕셔너리도 in 연산자로 키의 존재 여부를 확인할 수 있습니다.
    - dict1의 값을 수정하면서 병합합니다.

    **주의**
    - 함수 내부에서는 외부 전역 변수(var1, var2 등)를 직접 사용하지 마세요.
    - 반드시 dict1을 직접 수정해서 반환하세요.
    """
    # ===== Your code here =====
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value

    # ==========================

    return dict1

if __name__ == "__main__":
    var1 = {'a': 1, 'b': 2}
    var2 = {'b': 3, 'c': 4, 'd': 5}
    answer = solution(var1, var2)
    print(answer)
