class Person:
    """
    사람의 신체 정보를 저장하고, BMI를 계산하는 클래스
    생성자:
        - name (str): 이름
        - _height (int or float): 키 (cm 단위)
        - _weight (int or float): 몸무게 (kg 단위)
    메서드:
        - height (property):
            - _height 값을 반환
        - height (setter):
            - _height 값을 변경
        - weight (property):
            - _weight 값을 반환
        - weight (setter):
            - _weight 값을 변경
        - bmi (property):
            - 키와 몸무게를 기반으로 BMI를 계산하여 소수 첫째자리까지 반환
            - BMI 계산식: round(weight / (height / 100) ** 2, 1)
        - __str__:
            - 반환값 (str): 사람의 이름, 키, 몸무게를 문자열로 반환
            - Person 객체를 print 했을 때 아래와 같은 포맷으로 출력되어야 함
            - 예시: 홍길동 - 키: 175cm / 몸무게: 70kg
    """

    def __init__(self, name, height, weight):
        self.name = name
        self._height = height
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def bmi(self):
        return round(self.weight / (self.height / 100) ** 2, 1)

    def __str__(self):
        return f"{self.name} - 키: {self.height}cm / 몸무게: {self.weight}kg"
    
    
if __name__ == '__main__':
    p = Person("홍길동", 175, 70)
    print(p, "/ BMI:", p.bmi)
