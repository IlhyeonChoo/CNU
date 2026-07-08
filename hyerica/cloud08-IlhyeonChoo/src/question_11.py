def modify_tuple_list(t, list_index, value_index, new_value):
    """
    튜플(t) 안에 포함된 리스트의 특정 인덱스(value_index) 값을 new_value로 변경한 후
    변경된 튜플을 반환하는 함수이다.
    튜플 자체는 불변(immutable)이지만, 튜플 내부에 있는 가변(mutable) 객체인 리스트는 수정할 수 있다.
    (힌트: t[list_index][value_index] = new_value 형태로 리스트 내부 값을 수정하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      t: 리스트를 하나 이상 포함하는 튜플
      list_index: 수정할 리스트가 위치한 튜플의 인덱스
      value_index: 리스트 내에서 수정할 값의 인덱스
      new_value: 새로 넣을 값
    인자:
      t (tuple): 리스트를 포함하는 튜플
      list_index (int): 수정할 리스트가 위치한 인덱스
      value_index (int): 리스트 내에서 수정할 원소의 인덱스
      new_value: 새로 넣을 값
    반환값:
      tuple: 내부 리스트가 수정된 원래 튜플 (튜플 자체는 같은 객체)
    예시:
      >>> modify_tuple_list(([1, 2, 3], 'hello'), 0, 1, 99)
          ([1, 99, 3], 'hello')
      >>> modify_tuple_list(([10, 20], [30, 40]), 1, 0, 99)
          ([10, 20], [99, 40])
    """
    # ===== Your Code Here =====
    t[list_index][value_index] = new_value
    return t
    # ==========================

if __name__ == '__main__':
    t = ([1, 2, 3], 'hello')
    #### 함수 호출 ####
    result = modify_tuple_list(t, 0, 1, 99)
    print(f'수정된 튜플: {result}')
    print(f'원본 튜플(같은 객체): {t}')
    #################
