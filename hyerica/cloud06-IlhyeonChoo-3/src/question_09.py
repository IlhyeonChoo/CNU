def solution(dictionary):
    """
    **문제**
    - 딕셔너리 dictionary 안에는 어떤 사람의 신원정보(이름, 나이)가 저장되어 있습니다. 
      이때, 나이가 20세 이상이면 "adult"라는 새로운 키를 만들고 True 값을 저장하세요.
      만약, 20세 미만이라면, False를 저장하세요.
    - 예: dictionary가 {"name": "Alice", "age": 29} 이면, 이 dictionary를 수정하여
      {"name": "Alice", "age": 29, "adult": True}로 만들어야 합니다.

    **예상출력**
    - {'name': 'Alice', 'age': 29, 'adult': True}
    - {'name': 'Bob', 'age': 18, 'adult': False}
    - {'name': 'Charlie', 'age': 22, 'adult': True}
    """

    # ===== Your code here =====
    dictionary["adult"] = dictionary["age"] >= 20
    # ==========================

    return dictionary


if __name__ == "__main__":
    person_info = {
        "name": "Alice",
        "age": 29
    }
    person_info = solution(person_info)
    print(person_info)

    person_info = {
        "name": "Bob",
        "age": 18
    }
    person_info = solution(person_info)
    print(person_info)

    person_info = {
        "name": "Charlie",
        "age": 22
    }
    person_info = solution(person_info)
    print(person_info)

