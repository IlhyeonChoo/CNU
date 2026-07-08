"""
일곱개의 Time 객체가 주어졌을 때, 다음 출력이 나오도록 print 문을 완성하세요.
question_14에서 구현한 TimeComparator 클래스의 정적메서드들을 이용하여 구현하세요.

이때, 각 출력은 다음과 같은 의미입니다.
1. t1와 t2의 시간(hour)과 분(minute)이 같은지
2. t3와 t6의 시간(hour)과 분(minute)이 같은지
3. t2와 t5의 시간(hour)이 같은지
4. t2와 t7의 시간(hour)이 같은지
5. t2가 t5의 시간보다 이른시간인지

예상출력:
    False
    True
    False
    True
    False
"""

import sys, os
sys.path.append(os.path.dirname(__file__))


# ----- your code here -----
# question_13과 question_14를 임포트하세요.
import question_13
import question_14

# --------------------------


def main():
    t1 = question_13.Time.from_string("12:30:23")
    t2 = question_13.Time.from_string("09:33:13")
    t3 = question_13.Time.from_string("11:59:23")
    t4 = question_13.Time.from_string("13:44:13")
    t5 = question_13.Time.from_string("08:01:01")
    t6 = question_13.Time.from_string("11:59:23")
    t7 = question_13.Time.from_string("09:59:15")

    # ----- your code here -----
    print(question_14.TimeComparator.equals_hour_and_minute(t1, t2))
    print(question_14.TimeComparator.equals_hour_and_minute(t3, t6))
    print(question_14.TimeComparator.equals_hour(t2, t5))
    print(question_14.TimeComparator.equals_hour(t2, t7))
    print(question_14.TimeComparator.less_than(t2, t5))
    # --------------------------


if __name__ == "__main__":
    main()
