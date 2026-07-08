"""
다음의 Time 클래스는 시간, 분, 초 세 가지 정수를 입력받아 해당 시간정보를 저장하는 클래스입니다.
이때, 편의를 위해, '12:13:41'과 같은 형식의 문자열로도 Time 객체를 생성할 수 있게 from_string 이라는 클래스 메서드를 구현하세요.
시간 문자열은 항상 '12:13:41'의 형태이며, 유효한 시간값으로 주어진다고 가정합니다(시간은 0 ~ 23, 분은 0 ~ 59, 초은 0 ~ 59).

from_string 메서드는 클래스 메서드로, 다음과 같은 형태를 가집니다.

메서드 from_string (class method):
    '12:13:41'와 같은 형식의 문자열 time_string을 입력받아, hour, minute, second를 추출한 후, Time 객체를 새로 생성하여 반환하는 메서드입니다.

    인자:
        - time_string: '12:13:41'와 같은 형식의 문자열
    반환값:
        - Time 객체

    예:
        t1 = Time.from_string('12:13:41')
        print(t1.hour, t1.minute, t1.second)
        
        의 결과는
        
        12 13 41

        이 되어야 합니다.

참고:
    클래스 메서드의 첫 번째 인자는 cls 입니다. cls의 의미는 클래스 메서드가 소속된 클래스 그 자체 입니다 (여기서는 cls == Time).
    따라서, 클래스메서드 내에서 cls(12, 13, 41) 이렇게 호출하면, Time(12, 13, 41)를 호출하는 것과 정확히 같습니다 (Time 객체 생성).
    hour, minute, second는 반드시 정수 형태로 저장하세요. Time("12", "13", "41") 이런 객체가 생성되도록 하시면 안 됩니다.

예상출력:
    12 30 23
    9 12 41
    21 8 9
"""

class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    # ----- your code here -----
    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(":"))
        return cls(hour, minute, second)

    # --------------------------


if __name__ == "__main__":
    t1 = Time.from_string("12:30:23")
    t2 = Time.from_string("09:12:41")
    t3 = Time(21, 8, 9)
    
    print(t1.hour, t1.minute, t1.second)
    print(t2.hour, t2.minute, t2.second)
    print(t3.hour, t3.minute, t3.second)
