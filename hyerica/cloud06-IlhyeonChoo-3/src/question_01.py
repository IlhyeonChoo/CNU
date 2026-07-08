def solution():
    """
    **문제**
    - 다음과 같은 형태의 딕셔너리 dictionary를 생성하는 코드를 작성하세요.
      - 키: "names", 값: ["Alice", "Bob", "Charlie"]
      - 키: "age", 값: [29, 14, 22]
      - 키: "gender", 값: ["female", "male", "female"]
    - dictionary["names"]를 호출하면 ["Alice", "Bob", "Charlie"]를 반환되도록 해야 합니다.
    - dictionary["age"]를 호출하면 [29, 14, 22]를 반환되도록 해야 합니다.
    - dictionary["gender"]를 호출하면 ["female", "male", "female"]를 반환되도록 해야 합니다.

    **힌트**
    - key의 데이터타입은 문자열, value의 데이터타입은 리스트인 dictionary입니다.

    **예상출력**
    - names ['Alice', 'Bob', 'Charlie']
    - age [29, 14, 22]
    - gender ['female', 'male', 'female']
    """

    # ===== Your code here =====
    dictionary = {
        "names": ["Alice", "Bob", "Charlie"],
        "age": [29, 14, 22],
        "gender": ["female", "male", "female"],
    }
    # ==========================

    return dictionary


if __name__ == "__main__":
    res = solution()
    for key in res.keys():
        print(key, res[key])

