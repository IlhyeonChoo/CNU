class MenuItem:
    """
    메뉴 항목의 공통 속성을 정의하는 상위 클래스
    생성자:
        - name (str): 메뉴 이름
        - price (int): 가격
        - calories (int): 칼로리
    메서드:
        - __repr__:
            - 반환값 (str): MenuItem 객체를 개발자 친화적인 형식으로 표현한 문자열
            - 아래 print(menu)의 출력이 아래와 같은 포맷으로 출력되야 함
            - 예시: [MenuItem(name='딸기 케이크', price=4500, calories=350), MenuItem(name='아이스 아메리카노', price=3000, calories=5)]
    """

    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __repr__(self):
        return f"MenuItem(name='{self.name}', price={self.price}, calories={self.calories})"

class Dessert(MenuItem):
    """
    MenuItem 클래스를 상속받아 구현한 디저트 하위 클래스
    생성자:
        - name (str): 디저트 이름
        - price (int): 가격
        - calories (int): 칼로리
        - sugar_content (int): 당도 (1~10)
        - 상위 클래스의 생성자를 super()를 통해 호출하고, 당도를 추가로 저장
    메서드:
        - __str__:
            - 반환값 (str): 디저트 정보를 문자열로 반환하는 메서드
            - Dessert 객체를 print 했을 때 아래와 같이 출력되어야 함
            - 예시: [디저트] 딸기 케이크 - 4500원 / 350kcal (당도: 7)
    """

    def __init__(self, name, price, calories, sugar_content):
        super().__init__(name, price, calories)
        self.sugar_content = sugar_content

    def __str__(self):
        return f"[디저트] {self.name} - {self.price}원 / {self.calories}kcal (당도: {self.sugar_content})"

class Drink(MenuItem):
    """
    MenuItem 클래스를 상속받아 구현한 음료 하위 클래스
    생성자:
        - name (str): 음료 이름
        - price (int): 가격
        - calories (int): 칼로리
        - size (str): 음료 사이즈 (예: 'S', 'M', 'L')
        - 상위 클래스의 생성자를 super()를 통해 호출하고, 사이즈를 추가로 저장
    메서드:
        - __str__:
            - 반환값 (str): 음료 정보를 사용자 친화적인 형식으로 문자열로 반환
            - Drink 객체를 print 했을 때 아래와 같이 출력되어야 함
            - 예시: [음료] 아이스 아메리카노 - 3000원 / 5kcal (사이즈: M)
    """

    def __init__(self, name, price, calories, size):
        super().__init__(name, price, calories)
        self.size = size

    def __str__(self):
        return f"[음료] {self.name} - {self.price}원 / {self.calories}kcal (사이즈: {self.size})"

if __name__ == '__main__':
    menu = [
    Dessert("딸기 케이크", 4500, 350, 7),
    Drink("아이스 아메리카노", 3000, 5, 'M')
]
    print(menu)

    for item in menu:
        print(item)
