def solution(list_of_tuple):
    """
    **문제**
    - 튜플 (키, 값)으로 구성된 리스트 list_of_tuple을 이용하여 딕셔너리를 생성하는 코드를 작성하세요.
    - 딕셔너리는 dictionary 변수에 저장합니다.
    - list_of_tuple은 [(키1, 값1), (키2, 값2), ...] 이런 식으로 입력됩니다.
    - 튜플은 키, 값 두 가지 원소로 구성됩니다.
    - 리스트를 순회하지 말고 단 한줄의 코드로 작성하세요.

    **힌트**
    - 동영상강의 중 딕셔너리 생성 파트에 있습니다.

    **예상출력**
    =====
    orange 5
    mango 2
    apple 19
    =====
    pineapple 115
    durian 32
    grape 13
    =====
    watermelon 15
    melon 391
    blueberry 19
    """

    # ===== Your code here =====
    dictionary = dict(list_of_tuple)
    # ==========================

    return dictionary


if __name__ == "__main__":
    tuples = [("orange", 5), ("mango", 2), ("apple", 19)]
    res = solution(tuples)
    print("=====")
    for key in res.keys():
        print(key, res[key])

    tuples = [("pineapple", 115), ("durian", 32), ("grape", 13)]
    res = solution(tuples)
    print("=====")
    for key in res.keys():
        print(key, res[key])

    tuples = [("watermelon", 15), ("melon", 391), ("blueberry", 19)]
    res = solution(tuples)
    print("=====")
    for key in res.keys():
        print(key, res[key])

