import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_09 import group_by_city, get_city_average

def test():
    # 기본 케이스
    records = [('Seoul', 25), ('Busan', 28), ('Seoul', 23), ('Busan', 30), ('Incheon', 22)]
    city_temps = group_by_city(records)
    assert city_temps['Seoul'] == [25, 23]
    assert city_temps['Busan'] == [28, 30]
    assert city_temps['Incheon'] == [22]

    avg = get_city_average(city_temps)
    assert avg['Seoul'] == 24.0
    assert avg['Busan'] == 29.0
    assert avg['Incheon'] == 22.0

    # 한 도시에 기록이 1개만 있을 때 평균 = 그 값
    records2 = [('Daegu', 32)]
    ct2 = group_by_city(records2)
    assert ct2['Daegu'] == [32]
    assert get_city_average(ct2)['Daegu'] == 32.0

    # 도시가 1개만 있는 경우
    records3 = [('Jeju', 20), ('Jeju', 22), ('Jeju', 24)]
    ct3 = group_by_city(records3)
    assert ct3['Jeju'] == [20, 22, 24]
    assert get_city_average(ct3)['Jeju'] == 22.0

    # 기록 순서 보존 확인
    records4 = [('X', 10), ('Y', 20), ('X', 30), ('Y', 40), ('X', 50)]
    ct4 = group_by_city(records4)
    assert ct4['X'] == [10, 30, 50]
    assert ct4['Y'] == [20, 40]

    # 소수점 반올림 (round(..., 1))
    records5 = [('A', 10), ('A', 20), ('A', 30)]  # 평균 20.0
    ct5 = group_by_city(records5)
    assert get_city_average(ct5)['A'] == 20.0

    records6 = [('B', 10), ('B', 11)]  # 평균 10.5
    ct6 = group_by_city(records6)
    assert get_city_average(ct6)['B'] == 10.5
