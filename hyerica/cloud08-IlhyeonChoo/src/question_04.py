from collections import namedtuple

def create_students(data):
    """
    학생 데이터(data)를 받아 Student namedtuple 리스트를 생성하는 함수이다.
    함수 내에서 'name', 'korean', 'math', 'english' 필드를 가지는 Student namedtuple을 정의하고,
    입력된 데이터 리스트의 각 튜플을 사용하여 Student 객체를 생성한 후 리스트에 담아 반환한다.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      data: (이름, 국어점수, 수학점수, 영어점수) 튜플의 리스트
    인자:
      data (list): (이름, 국어점수, 수학점수, 영어점수) 튜플로 이루어진 리스트
    반환값:
      list: 각 요소가 Student namedtuple 객체인 리스트
    예시:
      >>> create_students([('Kim', 90, 85, 92), ('Lee', 95, 88, 97)])
          [Student(name='Kim', korean=90, math=85, english=92),
           Student(name='Lee', korean=95, math=88, english=97)]
    """
    # ===== Your Code Here =====
    Student = namedtuple('Student', ['name', 'korean', 'math', 'english'])
    return [Student(*student) for student in data]
    # ==========================

def get_top_student(students):
    """
    학생 목록(students)에서 세 과목 평균이 가장 높은 학생을 반환하는 함수이다.
    각 학생의 평균 점수를 (korean + math + english) / 3 으로 계산하시오.
    (힌트: max() 함수와 key 매개변수를 활용하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      students: Student namedtuple의 리스트
    인자:
      students (list): Student namedtuple의 리스트
    반환값:
      Student: 세 과목 평균 점수가 가장 높은 Student namedtuple
    예시:
      >>> get_top_student(student_list)
          Student(name='Lee', korean=95, math=88, english=97)
    """
    # ===== Your Code Here =====
    return max(
        students,
        key=lambda student: (student.korean + student.math + student.english) / 3,
    )
    # ==========================

if __name__ == '__main__':
    data = [('Kim', 90, 85, 92), ('Lee', 95, 88, 97), ('Park', 70, 75, 68)]
    #### 함수 호출 ####
    students = create_students(data)
    print(f'학생 목록: {students}')
    print(f'최우수 학생: {get_top_student(students)}')
    #################
