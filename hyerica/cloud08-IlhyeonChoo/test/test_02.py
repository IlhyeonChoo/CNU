import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_02 import check_shortage

def test():
    # 기본 케이스: 일부 품목 부족
    stock = {'apple': 5, 'banana': 3, 'milk': 1}
    order = {'apple': 3, 'banana': 5, 'milk': 4}
    assert check_shortage(stock, order) == {'banana': 2, 'milk': 3}

    # 재고에 없는 품목을 주문한 경우
    stock2 = {'pen': 10, 'notebook': 5}
    order2 = {'pen': 3, 'notebook': 8, 'eraser': 2}
    assert check_shortage(stock2, order2) == {'notebook': 3, 'eraser': 2}

    # 재고가 주문량보다 충분한 경우 → 부족 없음
    stock3 = {'a': 10, 'b': 20}
    order3 = {'a': 5, 'b': 10}
    assert check_shortage(stock3, order3) == {}

    # 재고와 주문이 정확히 같은 경우 → 부족 없음
    stock4 = {'rice': 5}
    order4 = {'rice': 5}
    assert check_shortage(stock4, order4) == {}

    # 재고는 있지만 주문한 품목이 전혀 없는 경우
    stock5 = {'water': 100}
    order5 = {'juice': 3}
    assert check_shortage(stock5, order5) == {'juice': 3}

    # 부족 수량 정확도 확인
    stock6 = {'x': 2}
    order6 = {'x': 10}
    assert check_shortage(stock6, order6) == {'x': 8}
