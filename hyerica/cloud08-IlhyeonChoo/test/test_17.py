import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_17 import build_tag_dict

def test():
    # 기본 케이스: 2개 항목
    items = [
        ({'python', 'beginner'}, 'Intro to Python'),
        ({'data', 'pandas'}, 'Data Analysis'),
    ]
    result = build_tag_dict(items)
    assert len(result) == 2
    assert frozenset({'python', 'beginner'}) in result
    assert frozenset({'data', 'pandas'}) in result
    assert result[frozenset({'python', 'beginner'})] == 'Intro to Python'
    assert result[frozenset({'data', 'pandas'})] == 'Data Analysis'

    # 3개 항목
    items2 = [
        ({'ml', 'ai'}, 'Machine Learning'),
        ({'web', 'flask'}, 'Web Dev'),
        ({'db', 'sql'}, 'Database'),
    ]
    result2 = build_tag_dict(items2)
    assert len(result2) == 3
    assert result2[frozenset({'ml', 'ai'})] == 'Machine Learning'

    # frozenset이 키로 사용 가능한지 확인 (hashable)
    items3 = [({'a', 'b', 'c'}, 'ABC')]
    result3 = build_tag_dict(items3)
    key = frozenset({'a', 'b', 'c'})
    assert key in result3
    assert result3[key] == 'ABC'

    # 태그 순서가 달라도 같은 frozenset
    items4 = [({'x', 'y'}, 'XY')]
    result4 = build_tag_dict(items4)
    assert result4[frozenset({'y', 'x'})] == 'XY'  # 순서 무관

    # 단일 태그
    items5 = [({'solo'}, 'Solo Course')]
    result5 = build_tag_dict(items5)
    assert result5[frozenset({'solo'})] == 'Solo Course'
