# ----- your code here -----
def path_join(*args):
    """
    임의개수의 디렉토리 이름, 파일이름이 주어졌을때, 이 이름 사이에 "/"를 삽입하는 코드를 작성하세요.
    이때, 함수의 입력은 리스트로 주어지지 않고, 가변인자로 주어져야 합니다.
    파일명은 항상 맨 마지막에 입력된다고 가정합니다.

    예:
        path_join("a", "b", "c.txt") -> "a/b/c.txt" (인자가 리스트로 묶여있지 않음)

    인자:
        - args: 디렉토리 이름 및 파일이름을 입력받을 가변인자    
    반환값:
        - path: "/"가 삽입된 파일경로 문자열
    """
    path = "/".join(args)
    return path

# --------------------------


if __name__ == "__main__":
    """
    예상출력:
        c:/Program Files/Microsoft/test.txt
        /usr/bin/gcc
    """
    
    print(path_join("c:", "Program Files", "Microsoft", "test.txt"))
    print(path_join("/usr", "bin", "gcc"))

    
