# ----- your code here -----
def format_string(string_data, **kwargs): 
    """
    문자열을 입력받아 문자열을 변환하는 함수를 작성하세요.

    기본적으로 format_string(string_data)는 string_data를 그대로 반환합니다.
    만약, format_string(string_data, prefix="??") 처럼 prefix라는 인자가 추가로 전달되면, prefix를 string_data 앞에 붙인 문자열을 반환하게 하세요.
    이때, prefix와 string_data 사이에는 스페이스 한 칸을 넣어주세요.
    만약, format_string(string_data, postfix="??") 처럼 postfix라는 인자가 추가로 전달되면, postfix를 string_data 뒤에 붙인 문자열을 반환하게 하세요.
    마찬가지로, postfix와 string_data 사이에는 스페이스 한 칸을 넣어주세요.
    함수의 인자는 string_data와 가변 키워드 인자 두 개만 입력받도록 합니다.

    prefix와 postfix가 동시에 입력될 수도 있게 해야 합니다.
    prefix와 postfix가 동시에 입력되면, string_data 앞에 prefix를 붙이고 string_data 뒤에 postfix를 붙인 문자열을 반환하게 하세요.
    prefix, string_data, postfix 사이에는 공백 한 칸이 있어야 합니다.
    완성된 문자열의 맨 앞과 맨 뒤에는 공백이 없어야 합니다.

    인자:
    - string_data: 문자열
    - kwargs: 추가 인자 옵션 (가변 키워드 인자)

    반환값:
    - new_string_data: 재정의된 문자열
    """

    parts = []

    if "prefix" in kwargs:
        parts.append(kwargs["prefix"])

    parts.append(string_data)

    if "postfix" in kwargs:
        parts.append(kwargs["postfix"])

    new_string_data = " ".join(parts)
    return new_string_data
# --------------------------


if __name__ == "__main__":
    """
    예상출력:
        <START_OF_SENTENCE> This is a sentence.
        This is a sentence. <END_OF_SENTENCE>
        <START_OF_SENTENCE> This is a sentence. <END_OF_SENTENCE>
    """
    
    print(format_string("This is a sentence."))
    print(format_string("This is a sentence.", prefix="<START_OF_SENTENCE>"))
    print(format_string("This is a sentence.", postfix="<END_OF_SENTENCE>"))
    print(format_string("This is a sentence.", prefix="<START_OF_SENTENCE>", postfix="<END_OF_SENTENCE>"))
    
