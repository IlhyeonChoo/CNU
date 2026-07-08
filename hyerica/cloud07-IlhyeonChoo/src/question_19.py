from collections import deque
import random

def temperature_generator():
    """
    ** 이 함수를 수정하지 마세요 **
    24도에서 28도 사이의 무작위 온도 값을 소수점 셋째 자리까지 반올림하여 무한히 생성하는 제너레이터 함수이다.
    while True 루프 안에서 random.uniform(24, 28)를 사용하여 난수를 생성하고 round() 함수로 반올림한 후, yield 키워드를 사용하여 값을 하나씩 반환한다.
    """
    while True:
        temperature = round(random.uniform(24, 28), 3)
        yield temperature

def run(temp_list, time):
    """
    지정된 시간(단계 수) 동안 온도 데이터를 시뮬레이션하여, 크기가 3으로 고정된 deque에 최신 온도 3개만 유지하는 함수이다.
    1. 함수 내에서 temperature_generator를 생성한다.
    2. 생성된 generator를 time 횟수만큼 반복하면서 온도 값을 얻는다. 
    3. deque의 크기가 3이면 가장 오른쪽(가장 오래된 데이터) 요소를 제거한 후, 새로운 온도 값을 왼쪽에 추가한다.
    4. deque의 크기가 3보다 작으면 바로 왼쪽에 추가한다.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      temp_list: 온도 값들을 저장하고 업데이트할 deque 객체
      time: 시뮬레이션을 반복할 횟수
    인자:
      temp_list (deque): 온도 값을 담을 deque 객체
      time (int): 시뮬레이션 반복 횟수
    반환값:
      없음
    동작 예시:
      >>> logs = deque()
      >>> run(logs, simulation_time)
      >>> print(logs)
      >>> deque([24.596, 24.365, 26.259]) (값은 매번 다름)
    """
    # ===== Your Code Here =====
    generator = temperature_generator()
    for _ in range(time):
        temperature = next(generator)
        if len(temp_list) == 3:
            temp_list.pop()
        temp_list.appendleft(temperature)
    # ==========================

if __name__ == '__main__':
    logs = deque()
    simulation_time = 10
    #### 함수 호출 ####
    run(logs, simulation_time)
    ################
    print(logs)
