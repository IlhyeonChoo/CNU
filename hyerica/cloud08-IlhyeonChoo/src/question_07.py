from collections import deque

def moving_average(numbers, window_size):
    """
    숫자 리스트(numbers)와 윈도우 크기(window_size)를 받아,
    각 시점에서의 이동 평균(moving average)을 계산하여 리스트로 반환하는 함수이다.
    deque(maxlen=window_size)를 사용하면 자동으로 오래된 값이 제거된다.
    윈도우가 window_size개로 채워진 이후부터 평균을 계산하여 결과 리스트에 추가하시오.
    (힌트: deque에 값을 추가하고, len(window) == window_size 이면 평균을 계산하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      numbers: 이동 평균을 계산할 숫자 리스트
      window_size: 이동 평균 계산에 사용할 윈도우 크기
    인자:
      numbers (list): 숫자 리스트
      window_size (int): 이동 평균 윈도우 크기
    반환값:
      list: 각 시점의 이동 평균 리스트 (window_size개가 채워진 시점부터 계산)
    예시:
      >>> moving_average([1, 2, 3, 4, 5], 3)
          [2.0, 3.0, 4.0]
      >>> moving_average([10, 20, 30, 40], 2)
          [15.0, 25.0, 35.0]
    """
    # ===== Your Code Here =====
    if window_size <= 0:
        return []

    window = deque(maxlen=window_size)
    averages = []
    current_sum = 0

    for number in numbers:
        if len(window) == window_size:
            current_sum -= window[0]

        window.append(number)
        current_sum += number

        if len(window) == window_size:
            averages.append(current_sum / window_size)

    return averages
    # ==========================

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    window_size = 3
    #### 함수 호출 ####
    print(f'이동 평균: {moving_average(numbers, window_size)}')
    #################
