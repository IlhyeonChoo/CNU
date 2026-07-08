def unpack_first_rest_last(t):
    """
    튜플(t)에서 첫 번째 원소, 중간 원소들, 마지막 원소를 분리하여 반환하는 함수이다.
    확장 언패킹(Extended Unpacking)의 * 연산자를 사용하시오.
    (힌트: first, *middle, last = t 형태로 언패킹하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      t: 3개 이상의 원소를 가진 튜플
    인자:
      t (tuple): 3개 이상의 원소를 가진 튜플
    반환값:
      tuple: (첫번째_원소, 중간원소_리스트, 마지막_원소) 형태의 튜플
    예시:
      >>> unpack_first_rest_last((1, 2, 3, 4, 5))
          (1, [2, 3, 4], 5)
      >>> unpack_first_rest_last(('a', 'b', 'c'))
          ('a', ['b'], 'c')
    """
    # ===== Your Code Here =====
    first, *middle, last = t
    return first, middle, last
    # ==========================

def swap_with_unpack(a, b):
    """
    두 값(a, b)을 튜플 언패킹을 이용하여 교환하고 교환된 결과를 튜플로 반환하는 함수이다.
    임시 변수를 사용하지 않고 a, b = b, a 형태의 튜플 언패킹으로 구현하시오.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      a: 첫 번째 값
      b: 두 번째 값
    인자:
      a: 첫 번째 값
      b: 두 번째 값
    반환값:
      tuple: (교환된_a, 교환된_b) — 즉 원래 b, a 순서
    예시:
      >>> swap_with_unpack(10, 20)
          (20, 10)
      >>> swap_with_unpack('hello', 'world')
          ('world', 'hello')
    """
    # ===== Your Code Here =====
    a, b = b, a
    return a, b
    # ==========================

if __name__ == '__main__':
    t = (1, 2, 3, 4, 5)
    #### 함수 호출 ####
    print(f'언패킹 결과: {unpack_first_rest_last(t)}')
    print(f'교환 결과: {swap_with_unpack(10, 20)}')
    #################
