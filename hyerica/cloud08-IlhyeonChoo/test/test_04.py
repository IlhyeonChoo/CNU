import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_04 import create_students, get_top_student

def test():
    data = [('Kim', 90, 85, 92), ('Lee', 95, 88, 97), ('Park', 70, 75, 68)]
    students = create_students(data)

    assert len(students) == 3
    assert students[0].name == 'Kim'
    assert students[0].korean == 90
    assert students[0].math == 85
    assert students[0].english == 92
    assert students[1].name == 'Lee'
    assert students[1].korean == 95
    assert students[1].math == 88
    assert students[1].english == 97
    assert students[2].name == 'Park'
    assert students[2].korean == 70
    assert students[2].math == 75
    assert students[2].english == 68

    top = get_top_student(students)
    assert top.name == 'Lee'  # (95+88+97)/3 = 93.3 최고점

    # 1명만 있는 경우
    single = create_students([('Choi', 80, 80, 80)])
    assert len(single) == 1
    assert get_top_student(single).name == 'Choi'

    # 최우수 학생이 첫 번째인 경우
    data2 = [('A', 100, 100, 100), ('B', 60, 60, 60), ('C', 70, 70, 70)]
    students2 = create_students(data2)
    assert get_top_student(students2).name == 'A'

    # 최우수 학생이 마지막인 경우
    data3 = [('X', 50, 50, 50), ('Y', 60, 70, 65), ('Z', 90, 95, 92)]
    students3 = create_students(data3)
    top3 = get_top_student(students3)
    assert top3.name == 'Z'  # (90+95+92)/3 = 92.3

    # namedtuple 필드 접근 방식 (인덱스와 속성 모두 가능)
    data4 = [('Ryu', 88, 92, 84)]
    s4 = create_students(data4)
    assert s4[0].name == s4[0][0]
    assert s4[0].korean == s4[0][1]
    assert s4[0].math == s4[0][2]
    assert s4[0].english == s4[0][3]
