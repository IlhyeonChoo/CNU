def city_location(cities, locations):
    """
    도시의 리스트 (C)와 각 도시의 위치 리스트 (L)을 입력 받는 함수이다.
    두 리스트를 다음과 같이 하나의 리스트로 합친다.
    [(도시, 위도, 경도), (도시, 위도, 경도), ...]
    (힌트: zip 사용)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      cities: 도시 이름을 담은 리스트
      locations: 각 도시의 위도와 경도의 튜플을 담은 리스트
    인자:
      cities (list): 도시 이름을 담은 리스트
      locations (list): 각 도시의 위도와 경도의 튜플을 담은 리스트
    반환값:
      list: [(도시, 위도, 경도), (도시, 위도, 경도), ...]
    예시:
      >>> city_location(C, L)
          [('Seoul',37.56,126.97), ('Busan', 35.17, 129.07), ...]
    """
    # ===== Your Code Here =====
    city_locations = [
        (city, latitude, longitude)
        for city, (latitude, longitude) in zip(cities, locations)
    ]
    # ==========================
    return city_locations

def get_location(cities, name):
    """
    city_location 함수의 리턴값과 특정 도시의 이름을 입력 받는 함수이다.
    도시의 이름과 위치를 반환한다.
    단, 존재하지 않는 도시의 경우 고려하지않음
    (힌트: 두개 이상의 값을 리턴할때 콤마로 구분하여 여러 값을 반환 할 수 있습니다.)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      cities: city_location 함수의 리턴값
      name: 도시의 이름
    인자:
      cities (list): city_location 함수의 리턴값 [(도시, 위도, 경도), (도시, 위도, 경도), ...] 형태의 리스트
      name (str): 도시의 이름
    반환값:
      tuple(name(str), location(tuple))
    예시:
      >>> get_location(city_locations, 'Seoul')
          ('Seoul', (37.56, 126.97))
    """
    # ===== Your Code Here =====
    for city, latitude, longitude in cities:
        if city == name:
            return city, (latitude, longitude)
    # ==========================

if __name__ == '__main__':
    C = ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Ulsan']
    L = [(37.56, 126.97), (35.17, 129.07), (37.45, 126.70), (35.87, 128.60), (35.54, 129.31)]

    #### 함수 호출 ####
    """
    출력결과:
    city_locations = city_location(C, L)
    city, location = get_location(city_locations, 'Seoul')
    print(f'Name of the city: {city}, Location: {location}')
    >>> Name of the city: Seoul, Location: (37.56, 126.97)
    """
    city_locations = city_location(C, L)
    city, location = get_location(city_locations, 'Seoul')
    print(f'Name of the city: {city}, Location: {location}')
    ################
