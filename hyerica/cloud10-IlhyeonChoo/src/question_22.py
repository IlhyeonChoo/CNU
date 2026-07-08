class User:
    """
    사용자 기본 정보를 저장하는 상위 클래스
    생성자:
        - name (str): 사용자 이름
        - email (str): 이메일 주소
    메서드:
        - __str__:
            - 반환값 (str): 이름과 이메일을 함께 출력
            - 예시: 홍길동 (hong@gmail.com)
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
    
class Student(User):
    """
    User 클래스를 상속받아 구현한 학생 하위 클래스
    생성자:
        - 상위 클래스의 생성자를 super()를 통해 호출
        - name (str): 학생 이름
        - email (str): 이메일 주소
        - enrolled_courses (list): 수강 중인 Course 객체들을 저장할 빈 리스트를 초기화 (매개변수 아님)
    메서드:
        - enroll:
            - course (Course): 수강할 강좌 객체
            - 함수 내부에서 enrolled_courses 리스트에 course를 추가
            - 함수 내부에서 course.add_student 함수를 호출하여 자기자신(self)를 추가
        - __str__:
            - 반환값 (str): 이름과 수강 중인 과목 수를 함께 출력
            - 예시: 홍길동 (수강 중: 2과목)
    """

    def __init__(self, name, email):
        super().__init__(name, email)
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)

    def __str__(self):
        return f"{self.name} (수강 중: {len(self.enrolled_courses)}과목)"
    
    
class Instructor(User):
    """
    User 클래스를 상속받아 구현한 강사 하위 클래스
    생성자:
        - 상위 클래스의 생성자를 super()를 통해 호출
        - name (str): 강사 이름
        - email (str): 이메일 주소
        - courses_teaching (list): 담당 중인 강좌들을 저장할 빈 리스트로 초기화 (매개 변수 아님)
    메서드:
        - assign_course:
            - course (Course): 담당할 강좌 객체
            - 함수 내부에서 course.instructor를 자기자신(self)로 할당
            - 함수 내부에서 courses_teaching 리스트에 course를 추가
    """

    def __init__(self, name, email):
        super().__init__(name, email)
        self.courses_teaching = []

    def assign_course(self, course):
        course.instructor = self
        self.courses_teaching.append(course)

class Course:
    """
    강좌 정보를 저장하고 학생 및 강사와 연결하는 클래스
    생성자:
        - title (str): 강좌 제목
        - instructor (Instructor or None): 담당 강사 (기본값 None으로 초기화) (매개변수 아님)
        - students (list): 수강 중인 학생들을 저장할 빈 리스트로 초기화 (매개변수 아님)
    메서드:
        - add_student:
            - student (Student): 등록할 학생 객체
            - 함수 내부에서 students 리스트에 수강생을 목록에 추가
        - full (property):
            - 반환값 (bool): 수강 인원이 30명을 초과하면 True, 아니면 False
        - __len__:
            - 반환값 (int): 현재 수강 중인 학생 수
        - __str__:
            - 반환값 (str): 강좌 정보와 수강생 수, 강사 이름을 함께 출력
            - 예시: Python 기초 - 이몽룡 (수강생 2명)
    """

    def __init__(self, title):
        self.title = title
        self.instructor = None
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    @property
    def full(self):
        return len(self.students) > 30

    def __len__(self):
        return len(self.students)

    def __str__(self):
        instructor_name = self.instructor.name if self.instructor is not None else "None"
        return f"{self.title} - {instructor_name} (수강생 {len(self)}명)"
    
if __name__ == '__main__':
    # 강사와 학생 생성
    instructor = Instructor("Kevin", "kev@edu.com")
    s1 = Student("Abby", "abby@gmail.com")
    s2 = Student("Bob", "bob@gmail.com")

    # 강좌 생성 및 연결
    course = Course("Python 기초")
    instructor.assign_course(course)

    # 수강 등록
    s1.enroll(course)
    s2.enroll(course)

    # 출력
    print("학생 정보:", s1)
    print("강사 정보:", instructor)
    print("강좌 정보:", course)
    print("수강 인원 초과 여부:", course.full)
