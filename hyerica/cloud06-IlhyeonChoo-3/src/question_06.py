def solution(dictionary, new_key, new_value):
    """
    **문제**
    - 키-값 쌍으로 이루어진 dictionary에서 새로운 키-값 쌍을 추가하는 코드를 작성하세요.
    - 새로운 키,값은 new_key, new_value로 각각 주어집니다.
    
    **예상출력**
    - {'apple': 2, 'orange': 3, 'pineapple': 10, 'pear': 9, 'mango': 5, 'watermelon': 7}
    - {'t-shirts': 39, 'long pants': 21, 'jeans': 30, 'shoes': 4, 'hat': 59, 'skirt': 19}
    - {'user_laptop': 31, 'user_desktop': 20, 'user_tablet': 13, 'user_linux': 12}
    """

    # ===== Your code here =====
    dictionary[new_key] = new_value
    # ==========================

    return dictionary


if __name__ == "__main__":
    my_dict = {
        "apple": 2,
        "orange": 3,
        "pineapple": 10,
        "pear": 9,
        "mango": 5,
    }
    my_dict = solution(my_dict, "watermelon", 7)
    print(my_dict)

    my_dict = {
        "t-shirts": 39,
        "long pants": 21,
        "jeans": 30,
        "shoes": 4,
        "hat": 59,
    }
    my_dict = solution(my_dict, "skirt", 19)
    print(my_dict)

    my_dict = {
        "user_laptop": 31,
        "user_desktop": 20,
        "user_tablet": 13,
    }
    my_dict = solution(my_dict, "user_linux", 12)
    print(my_dict)

