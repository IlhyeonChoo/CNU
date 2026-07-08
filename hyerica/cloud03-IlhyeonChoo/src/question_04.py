def create_dictionary(first_key, first_value,
                      second_key, second_value):
    """
    first_key와 second_key를 키로, first_value와 second_value를 값으로 갖는 딕셔너리를 생성하는 함수를 작성하세요.
    또, 생성한 딕셔너리를 first_key로 참조하여 반환된 값을 출력하세요.
    함수를 완성하신 후, visual studio code 우상단의 실행버튼을 클릭하여 이 파일을 실행(run)해보세요.
    정답출력: 다음 두 줄이 출력되어야 함
        출력결과: Bob
        { 'Name': 'Bob', 'Affiliation': 'Dept. of Artificial Intelligence, Hanyang University, ERICA' }

    코드작성방법:
    - 코드에서 "None"을 지우고 적절한 코드를 완성하세요.
    - 여기 작성하는 모든 코드는 들여쓰기가 동일하게 되어 있어야 합니다. (space 4개)
    - "이 부분의 코드를 완성하세요" 로 표시된 부분에만 코드를 작성해주세요.

    힌트:
    - 변수로 key, value를 지정하여 딕셔너리를 생성해줄 수도 있습니다.
      예:
      a = "key"
      b = "value"
      my_dict = {a: b}

    파라미터:
    - first_key: key값 (문자열)
    - first_value: value값 (문자열)
    - second_key: key값 (문자열)
    - second_key: value값 (문자열)

    반환:
    - my_dict: 생성한 딕셔너리
    """

    ##### 이 부분의 코드를 완성하세요 #####
    my_dict = {first_key:first_value, second_key:second_value}
    name = first_key
    print(my_dict[name]) # 딕셔너리를 first_key로 참조한 값 출력
    ################################

    return my_dict


if __name__ == "__main__":
    # 다음 두 줄이 출력되어야 함
    # 출력결과: Bob
    # { 'Name': 'Bob', 'Affiliation': 'Dept. of Artificial Intelligence, Hanyang University, ERICA' }
    print("출력결과: ", end="")
    returned_dict = create_dictionary("Name", "Bob", "Affiliation", "Dept. of Artificial Intelligence, Hanyang University, ERICA")
    print(returned_dict)


