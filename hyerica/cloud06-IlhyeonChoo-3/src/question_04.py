def solution(dictionary, key_to_remove):
    """
    **문제**
    - 키-값 쌍으로 이루어진 dictionary에서 특정 키와 그에 해당하는 값을 제거하는 코드를 작성하세요.

    **힌트**
    - del을 써도 되고, pop 메서드를 사용해도 됩니다.
    
    **예상출력**
    - {'A': 1, 'C': 3, 'D': 4, 'E': 5}
    - {'F': 1, 'G': 2, 'H': 3, 'J': 5}
    - {'K': 1, 'L': 2, 'N': 4, 'O': 5}
    """

    # ===== Your code here =====
    dictionary.pop(key_to_remove)
    # ==========================

    return dictionary


if __name__ == "__main__":
    my_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
    }
    print(solution(my_dict, "B"))

    my_dict = {
        "F": 1,
        "G": 2,
        "H": 3,
        "I": 4,
        "J": 5,
    }
    print(solution(my_dict, "I"))

    my_dict = {
        "K": 1,
        "L": 2,
        "M": 3,
        "N": 4,
        "O": 5,
    }
    print(solution(my_dict, "M"))

