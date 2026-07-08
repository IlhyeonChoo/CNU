def solution(numbers):
    """
    **문제**
    - 주어진 리스트(numbers)를 오름차순으로 정렬하고 두개의 sub-list로 나누어 하나의 리스트에 담아 반환하세요.
    - 리스트를 앞과 뒷부분으로 절반씩 나누되, 길이가 홀수일 경우 중간값은 뒷부분에 포함하세요.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 입력: [7, 2, 5, 10, 1]
    - 결과: [[1, 2], [5, 7, 10]] <<< 홀수 길이인 경우 중간값은 뒷부분에 포함
    - 입력: [7, 2, 5, 10]
    - 결과: [[2, 5], [7, 10]] <<< 짝수 길이인 경우 절반으로 나눔

    **힌트**
    - 리스트 정렬, 슬라이싱, 길이 나누기를 사용하면 풀 수 있습니다.
    - 중간 값의 인덱스를 구할때 리스트의 길이를 절반으로 나누면 됩니다.
    - 반환값은 [앞쪽 리스트, 뒤쪽 리스트] 형태의 이중 리스트입니다.

    **주의**
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    numbers.sort()
    result_list = []
    if len(numbers)%2 == 0:
        result1 = numbers[:len(numbers)//2]
        result2 = numbers[len(numbers)//2:]
        result_list.append(result1)
        result_list.append(result2)
    else :
        result1 = numbers[:len(numbers)//2]
        result2 = numbers[len(numbers)//2:]
        result_list.append(result1)
        result_list.append(result2)
    # ==========================
    return result_list


if __name__ == "__main__":
    """
    주석을 풀어 두가지 경우에 대해 테스트를 해보세요.
    """
    numbers = [7, 2, 5, 10, 1] # 홀수 길이 리스트
    # numbers = [7, 2, 5, 10] # 짝수 길이 리스트
    my_answer = solution(numbers)
    print(my_answer)