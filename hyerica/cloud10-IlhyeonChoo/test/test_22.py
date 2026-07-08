import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_22 import *

def test():
    # 강사와 학생 생성
    instructor = Instructor("Kevin", "kev@edu.com")
    s1 = Student("Abby", "abby@gmail.com")

    # 강좌 생성 및 연결
    course = Course("Python 기초")
    instructor.assign_course(course)

    # 수강 등록
    s1.enroll(course)

    # 출력
    assert s1.enrolled_courses[0] == course
    assert instructor.name == "Kevin"
    assert len(course) == 1
    assert course.full == False