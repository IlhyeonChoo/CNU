def preprocess_data(date_list, weather_list):
    """
    **문제**
    - 다음과 같은 표를 만들기 위해, 날마다 날씨를 기록해둔 데이터가 주어졌다고 가정합니다.

      |------------|---------|
      | Date       | Weather |
      |------------|---------|
      | 2020-03-04 | Sunny   |
      | 2020-03-05 | SUNNY   |
      | 2020-03-06 | cloudy  |
      | 2020-03-07 | Cloudy  |
      | 2020-03-07 | Rainy   |
      |------------|---------|

      이때, 날씨를 기록한 사람이 날마다 달라서, 누구는 맨 앞글자만 대문자로, 누구는 전부 대문자로, 누구는 전부 소문자로 날씨를 기록해두었습니다.
      이렇게 문자열 대소문자 규칙이 통일되지 않는 경우, 이후 데이터를 분석할때 예기치못한 오류가 발생할 수 있기 때문에, 하나의 형식으로 통일하려 합니다.
      weather의 모든 문자열을 소문자로 바꾸는 코드를 작성하세요.
    - date_list는 날짜들의 리스트입니다 (예: ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"])
    - weather_list는 날씨들의 리스트입니다 (예: ["Sunny", "SUNNY", "cloudy", "Cloudy", "Rainy"])
    - data_list와 weather_list의 길이는 같습니다.

    **힌트**
    - date_list는 건들필요 없습니다. weather_list만 순회하면서 소문자로 바꾸는 코드를 작성하세요.

    **예상출력**
    - Test case 1
      |------------|---------|
      | Date       | Weather |
      |------------|---------|
      | 2020-03-04 | sunny   |
      | 2020-03-05 | sunny   |
      | 2020-03-06 | cloudy  |
      | 2020-03-07 | cloudy  |
      |------------|---------|
    - Test case 2
      |------------|---------|
      | Date       | Weather |
      |------------|---------|
      | 2020-03-04 | rainy   |
      | 2020-03-05 | rainy   |
      | 2020-03-06 | cloudy  |
      | 2020-03-07 | cloudy  |
      |------------|---------|
    - Test case 3
      |------------|---------|
      | Date       | Weather |
      |------------|---------|
      | 2020-03-04 | sunny   |
      | 2020-03-05 | sunny   |
      | 2020-03-06 | cloudy  |
      | 2020-03-07 | cloudy  |
      |------------|---------|
    """

    # ===== Your code here =====
    # weather를 순회하면서 소문자로 바꾼 weather를 preprocess_weather에 넣어주세요(preprocessed_weather_list.append(weather)).
    preprocessed_weather_list = []

    for weather in weather_list:
        preprocessed_weather_list.append(weather.lower())
    # ==========================

    preprocessed_data = {
        "Date": date_list,
        "Weather": preprocessed_weather_list,
    }

    return preprocessed_data  


def pretty_print(preprocessed_data):
    """
    !편의상 구현한 함수. 건드실 필요 없습니다.

    아래 프린트문 중 print(f"| {date[i]:10s} | {weather[i]:7s} ") 의 의미는,
    - 오늘 배우신 문자열 포매팅 f"| {} | {} |" 의 형태입니다.
      (세로줄 세 개와 문자열 두 개 출력)
    - 두 개의 {} 자리에 출력될 문자열은 각각 date[i]와 weather[i] 입니다.
    - {date[i]:10s} -> date[i] 문자열을 출력하는데, 10칸에 맞춰서 출력하라는 의미입니다.
      만약, date[i]의 길이가 10보다 짧으면 공백으로 채워넣습니다.
      예: date[i]가 "2020-03" 이면 {date[i]:10s}는 "2020-03   "로 출력됩니다 (공백 3개 삽입되어 길이 10으로 맞춰짐).
    - {weather[i]:7s} -> weather[i] 문자열을 출력하는데, 7칸에 맞춰서 출력하라는 의미입니다. 
      만약, weather[i]의 길이가 7보다 짧으면 공백으로 채워넣습니다.
      예: weather[i]가 "cloudy" 이면 {weather[i]:7s}는 "cloudy "로 출력됩니다 (공백 1개 삽입되어 길이 7로 맞춰짐).
    """

    date = preprocessed_data["Date"]
    weather = preprocessed_data["Weather"]

    print("|------------|---------|")
    print("| Date       | Weather |")
    for i in range(len(date)):
        print(f"| {date[i]:10s} | {weather[i]:7s} ")
    print("|------------|---------|")


if __name__ == "__main__":
    print("Test case 1")
    date_list = ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"]
    weather_list = ["Sunny", "SUNNY", "cloudy", "Cloudy"]
    preprocessed_data = preprocess_data(date_list, weather_list)
    pretty_print(preprocessed_data)

    print("Test case 2")
    date_list = ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"]
    weather_list = ["RAINY", "rainy", "cloudy", "CLOUDY"]
    preprocessed_data = preprocess_data(date_list, weather_list)
    pretty_print(preprocessed_data)

    print("Test case 3")
    date_list = ["2020-03-04", "2020-03-05", "2020-03-06", "2020-03-07"]
    weather_list = ["SUNNY", "SUNNY", "CLOUDY", "Cloudy"]
    preprocessed_data = preprocess_data(date_list, weather_list)
    pretty_print(preprocessed_data)
