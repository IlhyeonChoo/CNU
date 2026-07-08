import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_01 import count_frequent_words

def test():
    # 기본 케이스: 2번 이상 등장한 단어만
    assert count_frequent_words("apple banana apple cherry banana apple", 2) == {'apple': 3, 'banana': 2}

    # min_count가 높아서 일부만 통과
    assert count_frequent_words("cat dog cat cat dog bird", 3) == {'cat': 3}

    # 두 단어가 동일 횟수로 기준 통과
    assert count_frequent_words("hello world hello world hello", 2) == {'hello': 3, 'world': 2}

    # min_count=1 → 모든 단어 포함
    assert count_frequent_words("x y z", 1) == {'x': 1, 'y': 1, 'z': 1}

    # min_count가 최대 빈도보다 높아서 결과가 빈 딕셔너리
    assert count_frequent_words("one two three", 5) == {}

    # 한 단어만 반복 → 그 단어만 반환
    assert count_frequent_words("go go go go", 3) == {'go': 4}

    # min_count 경계값: 정확히 min_count번 등장한 단어도 포함
    result = count_frequent_words("a b a b c", 2)
    assert result == {'a': 2, 'b': 2}
    assert 'c' not in result
