from collections import Counter

def check_shortage(stock, order):
    """
    현재 재고(stock)와 주문량(order)을 비교하여 부족한 상품과 그 부족 수량을 반환하는 함수이다.
    Counter 뺄셈(-)을 활용하면 음수 결과는 자동으로 제거되어 부족량만 남는다.
    (힌트: Counter(order) - Counter(stock) 를 계산하면 부족한 항목만 남는다)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      stock: 현재 재고 딕셔너리 {상품명: 수량}
      order: 주문 수량 딕셔너리 {상품명: 수량}
    인자:
      stock (dict): 현재 재고 {상품명: 수량}
      order (dict): 주문 수량 {상품명: 수량}
    반환값:
      dict: 부족한 상품과 부족 수량 {상품명: 부족수량}
    예시:
      >>> check_shortage({'apple': 5, 'banana': 3, 'milk': 1}, {'apple': 3, 'banana': 5, 'milk': 4})
          {'banana': 2, 'milk': 3}
    """
    # ===== Your Code Here =====
    shortage = Counter(order) - Counter(stock)
    return dict(shortage)
    # ==========================

if __name__ == '__main__':
    stock = {'apple': 5, 'banana': 3, 'milk': 1}
    order = {'apple': 3, 'banana': 5, 'milk': 4}
    #### 함수 호출 ####
    print(f'부족 재고: {check_shortage(stock, order)}')
    #################
