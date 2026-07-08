import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_10 import get_bestseller

def test():
    # 기본 케이스
    sales = ['shirt', 'pants', 'shirt', 'shoes', 'shirt', 'pants']
    best = get_bestseller(sales)
    assert best.name == 'shirt'
    assert best.count == 3

    # 다른 아이템이 1위
    sales2 = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
    best2 = get_bestseller(sales2)
    assert best2.name == 'banana'
    assert best2.count == 3

    # 아이템이 1개만 있는 경우
    sales3 = ['only']
    best3 = get_bestseller(sales3)
    assert best3.name == 'only'
    assert best3.count == 1

    # 모든 아이템이 동일한 경우
    sales4 = ['a', 'a', 'a', 'a']
    best4 = get_bestseller(sales4)
    assert best4.name == 'a'
    assert best4.count == 4

    # BestSeller namedtuple 필드 이름 확인
    sales5 = ['x', 'x', 'y']
    best5 = get_bestseller(sales5)
    assert hasattr(best5, 'name')
    assert hasattr(best5, 'count')
    assert best5.name == 'x'
    assert best5.count == 2

    # 판매 수 정확도
    sales6 = ['red', 'blue', 'red', 'red', 'green', 'blue', 'red']
    best6 = get_bestseller(sales6)
    assert best6.name == 'red'
    assert best6.count == 4
