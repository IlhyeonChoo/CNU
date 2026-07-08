def solution(dictionary):
    """
    **문제**
    - 키-값 쌍으로 이루어진 dictionary에서 모든 값들의 합(summation)을 구하는 코드를 작성하세요.
    - 예: {"apple": 2, "grape": 3} 이면, 최종 결과값 summation은 5가 되어야 합니다.

    **힌트**
    - 방법1: sum 함수를 사용
    - 방법2: for문을 사용하여, dictionary의 값(value)들을 순회하면서 합을 구함
    
    **예상출력**
    - 29
    - 153
    - 64
    """

    summation = 0

    # ===== Your code here =====
    summation = sum(dictionary.values())
    # ==========================

    return summation


if __name__ == "__main__":
    my_dict = {
        "apple": 2,
        "orange": 3,
        "pineapple": 10,
        "pear": 9,
        "mango": 5,
    }
    print(solution(my_dict))

    my_dict = {
        "t-shirts": 39,
        "long pants": 21,
        "jeans": 30,
        "shoes": 4,
        "hat": 59,
    }
    print(solution(my_dict))

    my_dict = {
        "user_laptop": 31,
        "user_desktop": 20,
        "user_tablet": 13,
    }
    print(solution(my_dict))

