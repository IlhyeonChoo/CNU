class LibraryItem:
    """
    도서관 자료의 공통 속성을 정의하는 상위 클래스
    생성자:
        - title (str): 자료 제목
        - item_id (int): 자료 고유 번호
    메서드:
        - borrow: 하위 클래스에서 대출 동작을 정의하기 위해 오버라이딩하는 메서드
            - 매개변수, 반환값, 출력 없음 (빈 메서드)
    """

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def borrow(self):
        pass

class Book(LibraryItem):
    """
    LibraryItem 클래스를 상속받아 구현한 Book 자료 클래스
    생성자:
        - 별도로 정의하지 않으며, 상위 클래스의 생성자를 그대로 사용
    메서드:
        - borrow: 책 대출 동작을 출력하는 메서드로, 상위 클래스의 메서드를 오버라이딩
            - 매개변수 없음, 반환값 없음
            - print문을 사용하여 아래와 같이 출력
            - 예시: 책 Python Programming 을(를) 대출합니다.
    """

    def borrow(self):
        print(f"책 {self.title} 을(를) 대출합니다.")

class DVD(LibraryItem):
    """
    LibraryItem 클래스를 상속받아 구현한 DVD 자료 클래스
    생성자:
        - 별도로 정의하지 않으며, 상위 클래스의 생성자를 그대로 사용
    메서드:
        - borrow: DVD 대출 동작을 출력하는 메서드로, 상위 클래스의 메서드를 오버라이딩
            - 매개변수 없음, 반환값 없음
            - print문을 사용하여 아래와 같이 출력
            - 예시: DVD Spider Man 을(를) 대출합니다.
    """

    def borrow(self):
        print(f"DVD {self.title} 을(를) 대출합니다.")
    

if __name__ == '__main__':
    b = Book('Python Programming', 123)
    b.borrow()
    d = DVD('Spider Man', 234)
    d.borrow()
