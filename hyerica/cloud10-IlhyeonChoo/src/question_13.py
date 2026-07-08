"""
question_12 에서 구현한 Time 클래스 코드를 복사해오세요. (임포트 하지마세요)
Time 클래스에 구현된 두 메소드는 사용자의 편의에 따라, 직접 시간, 분, 초를 더해주거나, 다른 Time 객체를 더할 수 있게 해줍니다.
그러나, 서로다른 이름의 두 메서드로 구현되었기 때문에, 사용자가 메서드 이름을 다 기억해줘야 한다는 문제점이 발생합니다.

이번 문제에서는 add 라는 이름의 통합 메서드를 구현하는데, 다른 Time를 입력받으면 Time 객체를 이용하여 시간을 더해주고,
그렇지 않으면 hour, minute, second로 시간을 업데이트하도록 하세요.
즉,
1. 인자로 주어진 other_time이 None이 아니면, other_time 으로 현 객체의 hour, minute, second를 업데이트
2. 인자로 주어진 other_time이 None이면, 인자로 주어진 hour, minute, second로 현 객체 시간을 업데이트

메서드 add
    other_time, hour, minute, second 네 개의 인자를 입력받고, 유효한 other_time이 입력되면, other_time으로 현 객체 시간을 업데이트하고,
    그렇지않으면, hour, minute, second 세 인자로 현 객체의 시간을 업데이트하세요.

    이때, 네 개의 인자는 모두 다음과 같은 default 값을 갖도록 하세요.
    - hour: 0
    - minute: 0
    - second: 0
    - other_time: None
    즉, add 메서드를 호출할때, 위 네 개의 인자 중 별다른 입력이 명시되지 않은 인자는 default 값이 대입되도록 하세요.

    메서드 몸통을 구현할때는 이미 구현한 add_time, add_time_obj를 활용하세요.

    인자:
        - hour: 더해줄 시간. 정수형식 (default: 0)
        - minute: 더해줄 분. 정수형식 (default: 0)
        - second: 더해줄 초. 정수형식 (default: 0)
        - other_time: Time 객체 (default: None)

    반환값:
        - 없음

    예:
        t1 = Time.from_string('12:13:41')
        t1.add()                                # 아무것도 더해주지 않음
        print(t1.hour, t1.minute, t1.second)    # 12 13 41
        t1.add(hour=2)                          # hour만 더해줌
        print(t1.hour, t1.minute, t1.second)    # 14 13 41

        t2 = Time.from_string('01:08:23')
        t1.add(other_time=t2)                   # Time 객체를 더해줌
        print(t1.hour, t1.minute, t1.second)    # 15 22 4
        t1.add(minute=8, second=23)             # minunte, second만 더해줌
        print(t1.hour, t1.minute, t1.second)    # 15 30 27

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

    def add(self, hour=0, minute=0, second=0, other_time=None):
        if other_time is not None:
            self.add_time_obj(other_time)
        else:
            self.add_time(hour, minute, second)

# --------------------------


if __name__ == "__main__":
    t1 = Time.from_string("12:30:23")
    t1.add(hour=2, minute=7, second=40)
    print(t1.hour, t1.minute, t1.second)

    t2 = Time.from_string("03:30:20")
    t1.add(other_time=t2)
    print(t1.hour, t1.minute, t1.second)
