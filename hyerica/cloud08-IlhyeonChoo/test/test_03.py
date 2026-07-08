import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from collections import Counter
from question_03 import combine_word_counts

def test():
    # 기본 케이스
    docs = [['cat', 'dog'], ['cat', 'bird'], ['dog', 'dog']]
    assert combine_word_counts(docs) == Counter({'dog': 3, 'cat': 2, 'bird': 1})

    # 문서마다 중복 단어 있음
    docs2 = [['a', 'b', 'a'], ['b', 'c'], ['c', 'c', 'a']]
    assert combine_word_counts(docs2) == Counter({'a': 3, 'c': 3, 'b': 2})

    # 단일 문서
    docs3 = [['hello', 'world', 'hello']]
    assert combine_word_counts(docs3) == Counter({'hello': 2, 'world': 1})

    # 모든 문서에 같은 단어만 있음
    docs4 = [['x'], ['x'], ['x']]
    assert combine_word_counts(docs4) == Counter({'x': 3})

    # 각 문서마다 다른 단어만 있음 → 모두 1회
    docs5 = [['alpha'], ['beta'], ['gamma']]
    result5 = combine_word_counts(docs5)
    assert result5['alpha'] == 1
    assert result5['beta'] == 1
    assert result5['gamma'] == 1

    # 빈 문서 리스트 포함
    docs6 = [['sun', 'moon'], [], ['sun']]
    assert combine_word_counts(docs6) == Counter({'sun': 2, 'moon': 1})

    # 합산 총합 확인
    docs7 = [['p', 'q', 'r'], ['p', 'q'], ['p']]
    result7 = combine_word_counts(docs7)
    assert result7['p'] == 3
    assert result7['q'] == 2
    assert result7['r'] == 1
