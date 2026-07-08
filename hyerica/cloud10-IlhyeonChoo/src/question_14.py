"""
시간관련 비교연산을 묶어놓은 TimeComparator 이라는 클래스를 구현하세요.

이때, TimeComparator 클래스는 별도의 시간이나 Time 객체를 저장하지 않으며(상태 저장 X), 오로지 "비교연산기"의 역할만 수행합니다.
이 클래스는 별도의 멤버변수를 관리하지 않고, __init__ 메서드는 구현하지 않으며, 어떠한 멤버함수(메서드)도 없습니다.

대신, TimeComparator 클래스는 외부로부터 Time 객체 두 개를 입력받아 두 Time 객체를 비교해주는 static method 만 가지도록 할 것입니다.

TimeComparator 클래스에 다음과 같은 세 개의 Time 객체간 비교연산을 구현하세요.
- equals_hour(t1, t2)               # t1과 t2의 시간(hour)이 같은지 판별
- equals_hour_and_minute(t1, t2)    # t1과 t2의 시간(hour)과 분(minute)이 같은지 판별
- less_than(t1, t2)                 # t1 시간이 t2 시간보다 작은지(이전 시간인지) 판별

이때, 각 정적메서드는 다음과 같은 형태를 가져야 합니다.

정적메서드 equals_hour:
    두 개의 Time 객체를 입력받아 두 객체에 저장된 hour가 같으면 True, 아니면 False 반환

    인자:
        - t1: Time 객체
        - t2: Time 객체
    반환값:
        - boolean: t1의 hour와 t2의 hour가 같으면 True, 아니면 False

정적메서드 equals_hour_and_minute:
    두 개의 Time 객체를 입력받아 두 객체에 저장된 hour과 minute가 같으면, True, 아니면 False 반환

    인자:
        - t1: Time 객체
        - t2: Time 객체
    반환값:
        - boolean: t1의 hour, minute와 t2의 hour, minute가 같으면 True, 아니면 False

정적메서드 less_than:
    두 개의 Time 객체를 입력받아 첫 번째 객체에 저장된 시간이 두 번째 객체에 저장된 시간보다 작은지(이른지) 판별

    인자:
        - t1: Time 객체
        - t2: Time 객체
    반환값:
        - boolean: t1의 시간이 t2의 시간보다 이른시간이면 True, 아니면 False (같은 시간이면 False)

예상출력:
    True
    False
    True
    False
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

# ----- your code here -----
# question_13를 import 하세요
import question_13

# --------------------------


# ----- your code here -----
class TimeComparator:

    @staticmethod
    def equals_hour(t1, t2):
        return t1.hour == t2.hour

    @staticmethod
    def equals_hour_and_minute(t1, t2):
        return t1.hour == t2.hour and t1.minute == t2.minute

    @staticmethod
    def less_than(t1, t2):
        return (t1.hour, t1.minute, t1.second) < (t2.hour, t2.minute, t2.second)

# --------------------------


if __name__ == "__main__":
    print(TimeComparator.equals_hour(question_13.Time.from_string("09:00:00"), question_13.Time.from_string("09:02:30")))
    print(TimeComparator.equals_hour(question_13.Time.from_string("08:00:00"), question_13.Time.from_string("09:02:30")))
    print(TimeComparator.equals_hour_and_minute(question_13.Time.from_string("08:00:00"), question_13.Time.from_string("08:00:30")))
    print(TimeComparator.equals_hour_and_minute(question_13.Time.from_string("08:00:00"), question_13.Time.from_string("08:01:30")))

