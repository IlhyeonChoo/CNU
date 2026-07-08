def set_operations(s1, s2):
    """
    두 집합(s1, s2)에 대해 합집합, 교집합, 차집합(s1 기준)을 계산하여 딕셔너리로 반환하는 함수이다.
    | (합집합), & (교집합), - (차집합) 연산자를 사용하여 구현하시오.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      s1: 첫 번째 집합
      s2: 두 번째 집합
    인자:
      s1 (set): 첫 번째 집합
      s2 (set): 두 번째 집합
    반환값:
      dict: 다음 세 가지 키를 가지는 딕셔너리
            'union'        : s1과 s2의 합집합 (|)
            'intersection' : s1과 s2의 교집합 (&)
            'difference'   : s1에서 s2를 뺀 차집합 (-)
    예시:
      >>> set_operations({1, 2, 3, 4}, {3, 4, 5, 6})
          {'union': {1, 2, 3, 4, 5, 6}, 'intersection': {3, 4}, 'difference': {1, 2}}
    """
    # ===== Your Code Here =====
    return {
        'union': s1 | s2,
        'intersection': s1 & s2,
        'difference': s1 - s2,
    }
    # ==========================

if __name__ == '__main__':
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    #### 함수 호출 ####
    result = set_operations(s1, s2)
    print(f'합집합: {result["union"]}')
    print(f'교집합: {result["intersection"]}')
    print(f'차집합: {result["difference"]}')
    #################
