import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_08 import build_inverted_index

def test():
    # 기본 케이스
    docs = ["cat dog", "dog bird", "cat bird cat"]
    index = build_inverted_index(docs)
    assert index['cat'] == [0, 2]
    assert index['dog'] == [0, 1]
    assert index['bird'] == [1, 2]

    # 단어가 한 문서에만 등장
    docs2 = ["apple", "banana apple", "cherry"]
    index2 = build_inverted_index(docs2)
    assert index2['apple'] == [0, 1]
    assert index2['banana'] == [1]
    assert index2['cherry'] == [2]

    # 한 문서에 같은 단어가 반복 → 문서 번호는 한 번만 기록
    docs3 = ["sun sun sun", "moon", "sun moon"]
    index3 = build_inverted_index(docs3)
    assert index3['sun'] == [0, 2]       # 0번 문서에서 3번 나와도 [0]만
    assert index3['moon'] == [1, 2]

    # 단일 문서
    docs4 = ["only one doc here"]
    index4 = build_inverted_index(docs4)
    assert index4['only'] == [0]
    assert index4['doc'] == [0]

    # 모든 문서에 같은 단어
    docs5 = ["go", "go", "go"]
    index5 = build_inverted_index(docs5)
    assert index5['go'] == [0, 1, 2]

    # 단어가 특정 문서에만 등장
    docs6 = ["a b c", "d e f", "g h i"]
    index6 = build_inverted_index(docs6)
    assert index6['a'] == [0]
    assert index6['d'] == [1]
    assert index6['g'] == [2]
    assert 'a' not in index6['d']  # 'a'는 1번 문서에 없음
