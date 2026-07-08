def add_prefix_to_string(string, prefix):
    """
    어떤 문자열(string)의 맨 앞에 어떤 접두사(prefix)를 추가하는 함수를 작성하세요.
    함수를 완성하신 후, visual studio code 우상단의 실행버튼을 클릭하여 이 파일을 실행(run)해보세요.
    정답출력: "programming language"
    
    코드작성방법:
    - 코드에서 "None"을 지우고 적절한 코드를 완성하세요.
    - 접두사와 문자열 사이에 공백은 자동으로 삽입되므로, 따로 공백을 더해주지 않아도 됩니다.
    - 여기 작성하는 모든 코드는 들여쓰기가 동일하게 되어 있어야 합니다. (space 4개)
    - "이 부분의 코드를 완성하세요" 로 표시된 부분에만 코드를 작성해주세요.

    파라미터:
    - string: 어떤 문자열
    - prefix: 문자열 앞에 붙일 접두사

    반환:
    - string_with_prefix: 접두사가 추가된 문자열
    """

    ##### 이 부분의 코드를 완성하세요 #####
    string_with_prefix = prefix + string
    ################################

    return string_with_prefix


if __name__ == "__main__":
    # "programming language" 가 출력되어야 함
    print(f"String가 'language' 이고, prefix가 'programming '일 경우, 결과는 {add_prefix_to_string('language', 'programming ')}.")
