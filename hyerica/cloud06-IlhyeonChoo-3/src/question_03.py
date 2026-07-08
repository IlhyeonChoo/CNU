def solution(dictionary):
    """
    **문제**
    - 키-값 쌍 여러개로 이루어진 dictionary로부터 키 집합을 구하는 코드를 작성하세요.
    
    **예상출력**
    - dict_keys(['A', 'B', 'C', 'D', 'E'])
    - dict_keys(['F', 'G', 'H', 'I', 'J'])
    - dict_keys(['K', 'L', 'M', 'N', 'O'])
    """

    # ===== Your code here =====
    keys = dictionary.keys()
    # ==========================

    return keys


if __name__ == "__main__":
    my_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
    }
    print(solution(my_dict))

    my_dict = {
        "F": 1,
        "G": 2,
        "H": 3,
        "I": 4,
        "J": 5,
    }
    print(solution(my_dict))

    my_dict = {
        "K": 1,
        "L": 2,
        "M": 3,
        "N": 4,
        "O": 5,
    }
    print(solution(my_dict))

