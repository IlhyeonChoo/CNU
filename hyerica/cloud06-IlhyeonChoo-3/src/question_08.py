def solution(dictionary, key):
    """
    **문제**
    - dictionary에서 key를 키로 하는 아이템을 제거하고, 그 아이템의 값(value)을 반환하는 코드를 작성하세요.
    - key는 dictionary의 키 집합에 반드시 존재합니다.
    - 딕셔너리에서 제거될 값을 미리 저장하고 해당 키값 쌍을 제거하는 방법도 있지만, 딕셔너리의 어떤 메서드를 사용하면
      단 한 줄의 코드로도 가능합니다. (키-값을 제거하면서 동시에 그 값을 반환하는 메서드)

    **힌트**
    - 동영상강의를 시청해주세요.
    
    **예상출력**
    2
    30
    20
    
    """

    # ===== Your code here =====
    removed_value = dictionary.pop(key)
    # ==========================

    return removed_value


if __name__ == "__main__":
    my_dict = {
        "apple": 2,
        "orange": 3,
        "pineapple": 10,
        "pear": 9,
        "mango": 5,
    }
    print(solution(my_dict, "apple"))

    my_dict = {
        "t-shirts": 39,
        "long pants": 21,
        "jeans": 30,
        "shoes": 4,
        "hat": 59,
    }
    print(solution(my_dict, "jeans"))

    my_dict = {
        "user_laptop": 31,
        "user_desktop": 20,
        "user_tablet": 13,
    }
    print(solution(my_dict, "user_desktop"))


