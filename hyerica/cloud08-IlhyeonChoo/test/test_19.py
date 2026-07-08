import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from collections import Counter
from question_19 import common_words_total_count

def test():
    # 기본 케이스: 공통 단어 1개
    # 'dog': text1에서 1번 + text2에서 2번 = 3번
    assert common_words_total_count("cat dog cat", "dog bird dog") == Counter({'dog': 3})

    # 공통 단어 2개
    # 'apple': 1+2=3, 'dog': 1+2=3
    assert common_words_total_count("cat dog cat apple", "dog bird dog apple apple") == Counter({'apple': 3, 'dog': 3})

    # 공통 단어 없음 → 빈 Counter
    result3 = common_words_total_count("hello world", "foo bar")
    assert result3 == Counter()

    # 두 텍스트가 완전히 같을 때 → 모든 단어가 공통
    result4 = common_words_total_count("a b c", "a b c")
    assert result4['a'] == 2
    assert result4['b'] == 2
    assert result4['c'] == 2

    # 한쪽에만 있는 단어는 제외
    result5 = common_words_total_count("x y z", "x w")
    assert 'x' in result5
    assert 'y' not in result5
    assert 'z' not in result5
    assert 'w' not in result5
    assert result5['x'] == 2  # text1에서 1번 + text2에서 1번

    # 공통 단어 합산 값 확인
    result6 = common_words_total_count("sun sun sun moon", "sun moon moon")
    # 공통: sun(3+1=4), moon(1+2=3)
    assert result6['sun'] == 4
    assert result6['moon'] == 3
