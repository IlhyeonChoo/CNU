# ----- your code here -----
def parse_string_to_int(string_list):
    """
    정수이지만 문자열로 구성된 리스트를 입력받아서, 정수의 리스트로 변환하는 함수를 작성하세요.
    string_list는 ["1", "2", "33"] 처럼 정수를 문자열로 표현한 데이터의 리스트입니다.
    map 함수를 이용하세요.

    인자:
    - string_list: 정수문자열의 리스트

    반환값:
    - int_list: 정수의 리스트
    """

    int_list = list(map(int, string_list))

    return int_list
# --------------------------


if __name__ == "__main__":
    """
    예상출력:
        [1, 33, 222]
        [13, 3413, 12222]
        [61, 2116, 7377, 312451]
    """
    
    string_list = ["1", "33", "222"]
    print(parse_string_to_int(string_list))
    
    string_list = ["13", "3413", "12222"]
    print(parse_string_to_int(string_list))
    
    string_list = ["61", "2116", "7377", "312451"]
    print(parse_string_to_int(string_list))
    
