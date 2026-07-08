import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_07 import moving_average

def test():
    # 기본 케이스: window=3
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]

    # window=2
    assert moving_average([10, 20, 30, 40], 2) == [15.0, 25.0, 35.0]

    # 리스트 길이 == window_size → 결과 1개
    assert moving_average([1, 2, 3], 3) == [2.0]

    # 모든 값이 같음 → 평균이 그 값
    assert moving_average([5, 5, 5, 5, 5], 4) == [5.0, 5.0]

    # window=1 → 각 원소 그대로 float
    assert moving_average([3, 6, 9], 1) == [3.0, 6.0, 9.0]

    # 결과 리스트 길이 검증: len(numbers) - window_size + 1
    result = moving_average([1, 2, 3, 4, 5, 6], 4)
    assert len(result) == 3
    assert result[0] == 2.5   # (1+2+3+4)/4
    assert result[1] == 3.5   # (2+3+4+5)/4
    assert result[2] == 4.5   # (3+4+5+6)/4

    # 음수 포함
    assert moving_average([-3, -1, 1, 3], 2) == [-2.0, 0.0, 2.0]

    # window_size가 리스트 길이와 동일
    assert moving_average([10, 20, 30], 3) == [20.0]
