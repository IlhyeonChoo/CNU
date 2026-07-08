"""
question_11 에서 구현한 Time 클래스 코드를 복사해오세요. (임포트 하지마세요)
Time 클래스에, 다음과 같이 시간을 더해주는 두 개의 메서드를 추가로 구현하세요.

메서드 add_time
    더해줄 시간(hour), 분(minute), 초(second)를 입력받아, 현 객체에 저장된 hour, minute, second에 더해주는 메서드입니다.
    이때, 인자로 들어오는 hour, minute, second는 항상 정수형태이며, 유효한 시간값(hour < 24, minute < 60, second < 60)이 들어온다고 가정합니다.

    만약, 시간을 더해준 후, 시간범위가 초과되면(hour >= 24 or minute >= 60 or second >= 60), 알맞게 시간을 조정해주세요.
    예를들어, second가 60을 초과하면, second에서 60을 빼주신 후, minute에 1을 더해주셔야 합니다.

    인자:
        - hour: 더해줄 시간. 정수형식
        - minute: 더해줄 분. 정수형식
        - second: 더해줄 초. 정수형식

    반환값:
        - 없음

메서드 add_time_obj
    이번에는 더해줄 시간 객체를 입력받아, 현 객체에 저장된 hour, minute, second에 더해주는 메서드입니다.
    이때, 인자로 들어오는 Time 객체에 저장된 hour, minute, second는 항상 정수형태이며, 유효한 시간값(hour < 24, minute < 60, second < 60)을 가진다고 가정합니다.

    만약, 시간을 더해준 후, 시간범위가 초과되면(hour >= 24 or minute >= 60 or second >= 60), 알맞게 시간을 조정해주세요.
    예를들어, second가 60을 초과하면, second에서 60을 빼주신 후, minute에 1을 더해주셔야 합니다.

    인자:
        - other_time: Time 객체

    반환값:
        - 없음

예상출력:
    14 38 3
    18 8 23
"""

# ----- your code here -----
class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(":"))
        return cls(hour, minute, second)

    def add_time(self, hour, minute, second):
        total_seconds = (
            self.hour * 3600
            + self.minute * 60
            + self.second
            + hour * 3600
            + minute * 60
            + second
        ) % (24 * 3600)
        self.hour = total_seconds // 3600
        self.minute = total_seconds % 3600 // 60
        self.second = total_seconds % 60

    def add_time_obj(self, other_time):
        self.add_time(other_time.hour, other_time.minute, other_time.second)

# --------------------------


if __name__ == "__main__":
    t1 = Time.from_string("12:30:23")
    t1.add_time(2, 7, 40)
    print(t1.hour, t1.minute, t1.second)

    t2 = Time.from_string("03:30:20")
    t1.add_time_obj(t2)
    print(t1.hour, t1.minute, t1.second)
