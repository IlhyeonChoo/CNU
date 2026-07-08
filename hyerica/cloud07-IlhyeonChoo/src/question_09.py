def calculate():
    """
    9주차 퀴즈에서 구현했던 계산기 함수를 함수화하세요.
    사용자로부터 "32 + 3" 와 같이 입력을 받으면, 해당 연산을 계산한 결과를 출력하는 코드를 구현하세요.
    사용자 입력은 반드시 "{숫자} {연산자} {숫자}"의 형식이며, 숫자와 연산자 사이는 공백 한 칸이 존재합니다.
    사용자가 exit를 입력할때까지 반복하다가, exit를 입력하면 루프를 탈출합니다.

    이때, 다음의 추가 함수를 구현하세요.
    - is_valid_input 함수
        사용자가 입력한 문자열이 "{숫자} {연산자} {숫자}" 형식인지 검사하는 함수
        다음 세 가지를 검사하고 모두 통과하면 True를 반환하세요.
        1. input_string을 split한 후 그 길이가 3이어야 함
        2. input_string을 split한 것에서, 첫번째와 세번째 문자열이 숫자여야 함( ?.isdigit() 메서드 활용)
        3. input_string을 split한 것에서, 두 번째 문자열이 +, -, *, / 중 하나여야 함

        인자:
            - input_string: 사용자가 입력한 문자열
        반환값:
            - is_valid: 입력한 문자열이 "{숫자} {연산자} {숫자}"의 형식이면 True, 아니면 False 반환
    - parse_input 함수
        사용자 입력을 operator, num1, num2로 분리하는 함수. 이때, operator는 문자열 타입, num1, num2는 float 타입이어야 합니다.
        split 함수와 float 함수를 적절히 사용하세요.

        인자:
            - input_string: 사용자가 입력한 문자열
        반환값
            - (operator, num1, num2): 사용자가 입력한 문자열로부터 분리한 연산자와 숫자1와 숫자2를 담은 튜플
    - execute_operation 함수
        operator, num1, num2 세 입력을 받아서 실제 연산을 수행하는 함수
        인자:
            - operator: 연산자
            - num1: 숫자1
            - num2: 숫자2
        반환값:
            - result: 연산 결과 (숫자)
    인자:
    - 없음

    반환값:
    - 없음
    """
    
    while True:
        input_string = input()

        if input_string.lower() == "exit":
            break

        if not is_valid_input(input_string):
            continue

        parsed_input = parse_input(input_string)
        result = execute_operation(*parsed_input)
        print(result)


# ----- Your code here -----
def is_valid_input(input_string):
    splitted = input_string.split()

    if len(splitted) != 3:
        return False

    num1, operator, num2 = splitted
    return num1.isdigit() and num2.isdigit() and operator in {"+", "-", "*", "/"}


def parse_input(input_string):
    num1, operator, num2 = input_string.split()
    return operator, float(num1), float(num2)


def execute_operation(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    return num1 / num2



# --------------------------


if __name__ == "__main__":
    """
    예상출력:
        1 + 2 (사용자입력)
        3.0
        3 + 4 (사용자입력)
        7.0
        3 / 4 (사용자입력)
        0.75
        3 * 4 (사용자입력)
        12.0
        3 // 3 (사용자입력 -> 출력없음)
        3 / 3 (사용자입력)
        1.0
        ee (사용자입력 -> 출력없음)
        exit (사용자입력 -> 종료)
    """
    calculate()    

    
