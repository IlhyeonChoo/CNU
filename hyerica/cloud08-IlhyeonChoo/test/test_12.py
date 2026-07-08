import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_12 import shallow_copy_result, deep_copy_result

def test():
    # 얕은 복사: 내부 리스트 공유 → 복사본 수정 시 원본도 변경됨
    orig_val, copy_val = shallow_copy_result([[1, 2, 3], [4, 5, 6]])
    assert orig_val == 99   # 원본도 99로 바뀜
    assert copy_val == 99   # 복사본도 99

    # 깊은 복사: 내부까지 독립 복사 → 원본 불변
    orig_val2, copy_val2 = deep_copy_result([[1, 2, 3], [4, 5, 6]])
    assert orig_val2 == 1   # 원본은 그대로
    assert copy_val2 == 99  # 복사본만 변경

    # 얕은 복사: 외부 리스트는 다른 객체, 내부 리스트는 공유 확인
    original = [[10, 20], [30, 40]]
    import copy
    shallow = copy.copy(original)
    assert shallow is not original          # 외부 리스트는 다른 객체
    assert shallow[0] is original[0]       # 내부 리스트는 같은 객체(공유)

    # 깊은 복사: 외부, 내부 모두 독립 객체
    original2 = [[10, 20], [30, 40]]
    deep = copy.deepcopy(original2)
    assert deep is not original2           # 외부 리스트도 다른 객체
    assert deep[0] is not original2[0]    # 내부 리스트도 다른 객체

    # 깊은 복사 후 복사본을 수정해도 원본 불변
    original3 = [[5, 6], [7, 8]]
    deep2 = copy.deepcopy(original3)
    deep2[0][0] = 999
    assert original3[0][0] == 5  # 원본 그대로
