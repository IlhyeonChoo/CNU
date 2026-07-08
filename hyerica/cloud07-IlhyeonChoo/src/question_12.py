def calculate_stats(numbers):
    """
    정수형 숫자를 담은 리스트를 입력 받는 함수이다.
    해당 리스트의 최솟값, 최댓값, 평균값을 모두 계산하여 한번에 반환하시오.
    (힌트: 콤마로 구분하여 여러값을 한번에 반환 할 수 있습니다.)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      numbers: 정수형 숫자를 담은 리스트
    인자:
      numbers (list): 정수형 숫자를 담은 리스트
    반환값:
      tuple: 최솟값(int), 최댓값(int), 평균값(float)
    예시:
      >>> calculate_stats(num_list)
          (1, 10, 5.5)
    """
    # ===== Your Code Here =====
    min_val = min(numbers)
    max_val = max(numbers)
    mean = sum(numbers) / len(numbers)
    # ==========================
    return min_val, max_val, mean

if __name__ == '__main__':
    num_list = [1,2,3,4,5,6,7,8,9,10]
    #### 함수 호출 ####
    min_val, max_val, mean = calculate_stats(num_list)
    ################
    print(min_val, max_val, mean)
