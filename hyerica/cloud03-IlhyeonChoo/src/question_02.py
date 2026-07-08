def convert_to_string(number):
    """
    number에 저장된 숫자를 문자열로 변환하는 함수를 작성하세요.
    함수를 완성하신 후, visual studio code 우상단의 실행버튼을 클릭하여 이 파일을 실행(run)해보세요.
    정답출력: <class 'str'> 123

    코드작성방법:
    - 코드에서 "None"을 지우고 적절한 코드를 완성하세요.
    - 여기 작성하는 모든 코드는 들여쓰기가 동일하게 되어 있어야 합니다. (space 4개)
    - "이 부분의 코드를 완성하세요" 로 표시된 부분에만 코드를 작성해주세요.

    파라미터:
    - number: 어떤 숫자

    반환:
    - string: 문자열 형태로 변환된 숫자 (type: 문자열)
    """

    ##### 이 부분의 코드를 완성하세요 #####
    string = str(number)
    ################################

    return string


if __name__ == "__main__":
    string = convert_to_string(123)
    # <class 'str'> 123 이 출력되어야 함
    print(type(string), string)

