from collections import defaultdict

def group_by_city(records):
    """
    도시별 온도 기록(records)을 받아 도시 이름을 키로, 온도 리스트를 값으로 하는
    defaultdict를 생성하여 반환하는 함수이다.
    (힌트: defaultdict(list) 사용)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      records: (도시이름, 온도) 튜플의 리스트
    인자:
      records (list): (도시이름, 온도) 형태의 튜플로 이루어진 리스트
    반환값:
      defaultdict: {도시이름: [온도 리스트]} 형태의 defaultdict(list)
    예시:
      >>> group_by_city([('Seoul', 25), ('Busan', 28), ('Seoul', 23), ('Busan', 30)])
          defaultdict(<class 'list'>, {'Seoul': [25, 23], 'Busan': [28, 30]})
    """
    # ===== Your Code Here =====
    city_temps = defaultdict(list)
    for city, temperature in records:
        city_temps[city].append(temperature)
    return city_temps
    # ==========================

def get_city_average(city_temps):
    """
    도시별 온도 딕셔너리(city_temps)에서 각 도시의 평균 온도를 계산하여 반환하는 함수이다.
    평균 온도는 소수점 첫째 자리까지 반올림하여 저장하시오.
    (힌트: round(sum(temps) / len(temps), 1) 활용)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      city_temps: {도시이름: [온도 리스트]} 형태의 딕셔너리 (group_by_city의 반환값)
    인자:
      city_temps (dict): 도시별 온도 리스트 딕셔너리
    반환값:
      dict: {도시이름: 평균온도} 형태의 딕셔너리
    예시:
      >>> get_city_average({'Seoul': [25, 23], 'Busan': [28, 30]})
          {'Seoul': 24.0, 'Busan': 29.0}
    """
    # ===== Your Code Here =====
    return {
        city: round(sum(temperatures) / len(temperatures), 1)
        for city, temperatures in city_temps.items()
    }
    # ==========================

if __name__ == '__main__':
    records = [('Seoul', 25), ('Busan', 28), ('Seoul', 23), ('Busan', 30), ('Incheon', 22)]
    #### 함수 호출 ####
    city_temps = group_by_city(records)
    print(f'도시별 온도: {dict(city_temps)}')
    print(f'도시별 평균: {get_city_average(city_temps)}')
    #################
