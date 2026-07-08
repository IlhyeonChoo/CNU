class Item:
    """
    상품 정보를 저장하고, 단가와 수량을 제어하는 클래스
    생성자:
        - name (str): 상품 이름
        - _price (int): 상품 단가
        - _quantity (int): 상품 수량
    메서드:
        - price (property):
            - _price 값을 반환
        - price (setter):
            - _price 값을 변경
        - quantity (property):
            - _quantity 값을 반환
        - quantity (setter):
            - _quantity 값을 변경
        - __str__:
            - 반환값 (str): 상품 정보를 문자열로 반환
            - Item 객체를 print 했을 때 아래와 같은 포맷으로 출력되어야 함
            - 예시: 콜라 (단가: 1500원, 수량: 3개)
    """    

    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return f"{self.name} (단가: {self.price}원, 수량: {self.quantity}개)"
    

if __name__ == '__main__':
    item = Item("콜라", 1500, 3)
    print(item)

    # Setter
    item.quantity = 5
    item.price = 2000
    print(item)
