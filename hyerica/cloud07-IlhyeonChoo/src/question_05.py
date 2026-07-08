

global_counter = 0

def preprocess_data(data):
    """
    함수 내에서 전역변수 global_counter의 값을 1 증가시키는 코드를 작성하세요.
    return은 사용하지마세요.
    """

    # ----- Your code here -----
    global global_counter
    global_counter += 1
    # --------------------------

    print(f"데이터 처리: {data}")


if __name__ == "__main__":
    """
    예상출력:
        데이터 처리: x0
        데이터 처리: x1
        데이터 처리: x2
        데이터 처리: x3
        데이터 처리: x4
        총 데이터처리 횟수: 5
        데이터 처리: x0
        데이터 처리: x1
        데이터 처리: x2
        데이터 처리: x3
        데이터 처리: x4
        총 데이터처리 횟수: 10
        데이터 처리: x0
        데이터 처리: x1
        데이터 처리: x2
        데이터 처리: x3
        데이터 처리: x4
        총 데이터처리 횟수: 15
    """
    
    for i in range(5):
        preprocess_data(f"x{i}")

    print(f"총 데이터처리 횟수: {global_counter}")
    
    for i in range(5):
        preprocess_data(f"x{i}")

    print(f"총 데이터처리 횟수: {global_counter}")

    for i in range(5):
        preprocess_data(f"x{i}")

    print(f"총 데이터처리 횟수: {global_counter}")
