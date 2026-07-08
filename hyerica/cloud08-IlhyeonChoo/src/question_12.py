import copy

def shallow_copy_result(original):
    """
    중첩 리스트를 포함한 리스트(original)의 얕은 복사(shallow copy)를 수행하고,
    복사본의 첫 번째 내부 리스트의 첫 번째 값을 99로 변경한 후,
    원본의 첫 번째 내부 리스트 첫 번째 값과 복사본의 해당 값을 튜플로 묶어 반환하는 함수이다.
    (힌트: copy.copy()로 얕은 복사 수행. 얕은 복사는 내부 객체를 공유하므로 원본도 영향을 받는다)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      original: 리스트를 내부 원소로 포함하는 리스트 (예: [[1, 2, 3], [4, 5, 6]])
    인자:
      original (list): 중첩 리스트
    반환값:
      tuple: (원본_첫원소_첫값, 복사본_첫원소_첫값) — 얕은 복사로 인해 두 값이 같다
    예시:
      >>> shallow_copy_result([[1, 2, 3], [4, 5, 6]])
          (99, 99)
    """
    # ===== Your Code Here =====
    copied = copy.copy(original)
    copied[0][0] = 99
    return original[0][0], copied[0][0]
    # ==========================

def deep_copy_result(original):
    """
    중첩 리스트를 포함한 리스트(original)의 깊은 복사(deep copy)를 수행하고,
    복사본의 첫 번째 내부 리스트의 첫 번째 값을 99로 변경한 후,
    원본의 첫 번째 내부 리스트 첫 번째 값과 복사본의 해당 값을 튜플로 묶어 반환하는 함수이다.
    (힌트: copy.deepcopy()로 깊은 복사 수행. 깊은 복사는 내부 객체까지 독립적으로 복사한다)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      original: 리스트를 내부 원소로 포함하는 리스트 (예: [[1, 2, 3], [4, 5, 6]])
    인자:
      original (list): 중첩 리스트
    반환값:
      tuple: (원본_첫원소_첫값, 복사본_첫원소_첫값) — 깊은 복사로 원본은 변경되지 않는다
    예시:
      >>> deep_copy_result([[1, 2, 3], [4, 5, 6]])
          (1, 99)
    """
    # ===== Your Code Here =====
    copied = copy.deepcopy(original)
    copied[0][0] = 99
    return original[0][0], copied[0][0]
    # ==========================

if __name__ == '__main__':
    original = [[1, 2, 3], [4, 5, 6]]
    #### 함수 호출 ####
    print(f'얕은 복사 결과 (원본, 복사본): {shallow_copy_result([[1, 2, 3], [4, 5, 6]])}')
    print(f'깊은 복사 결과 (원본, 복사본): {deep_copy_result([[1, 2, 3], [4, 5, 6]])}')
    #################
