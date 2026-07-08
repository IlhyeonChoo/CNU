class Recipe:
    """
    요리 이름과 재료 목록을 정의하는 상위 클래스
    생성자:
        - name (str): 요리 이름
        - ingredients (list of str): 재료 목록
    메서드:
        - show_info: 요리 이름과 재료를 출력하는 메서드
            - 매개변수 없음, 반환값 없음
            - print문을 사용하여 아래와 같이 출력
            - 예시: 김치찌개: 김치, 돼지고기, 양파
    """

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def show_info(self):
        print(f"{self.name}: {', '.join(self.ingredients)}")
    
class KoreanRecipe(Recipe):
    """
    Recipe 클래스를 상속받아 구현한 KoreanRecipe 하위 클래스
    생성자:
        - name (str): 요리 이름
        - ingredients (list of str): 재료 목록
        - spice_level (int): 매운맛 단계 (1~5 사이의 정수)
        - 상위 클래스의 생성자를 super()를 통해 호출하고, 매운맛 단계를 저장
    메서드:
        - show_info: 한식 스타일로 매운맛과 재료 정보를 출력하는 메서드로, 상위 클래스의 메서드를 오버라이딩
            - 매개변수 없음, 반환값 없음
            - print문을 사용하여 아래와 같이 출력
            - 예시: [한식] 김치찌개 (매운맛: ***) 재료: 김치, 돼지고기, 양파
    """

    def __init__(self, name, ingredients, spice_level):
        super().__init__(name, ingredients)
        self.spice_level = spice_level

    def show_info(self):
        spice = "*" * self.spice_level
        print(f"[한식] {self.name} (매운맛: {spice}) 재료: {', '.join(self.ingredients)}")
    

if __name__ == '__main__':
    kimchi_soup = KoreanRecipe('김치찌개', ['김치', '돼지고기', '양파'], 3)
    kimchi_soup.show_info()
