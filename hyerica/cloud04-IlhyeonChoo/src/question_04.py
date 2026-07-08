def path_join(list_of_dirs):
    r"""
    **문제**
    - 컴퓨터 디렉토리(폴더)들의 리스트가 주어졌을 때, 이들을 하나의 '경로' 문자열로 합치는 코드를 작성하세요.
    - list_of_dirs는 ["C:", "Users", "myname", "Documents"] 처럼 디렉토리 이름의 리스트로 구성되어 있습니다.
      이 문자열들을 "C:/Users/myname/Documents" 처럼 하나로 합치는 코드를 작성하세요.
    - 경로 구분자는 "/" 로 하세요 ("." 키의 바로 오른쪽).
    
    **힌트**
    - 문자열의 join 메서드를 활용하세요.
    - ".".join(["AA", "BB"]) => "AA.BB"  # 두 문자열 사이에 '.' 이 삽입되면서 하나의 문자열로 합쳐짐

    **예상출력**
    - Test case 1
    -     C:/Users/myname/Documents
    - Test case 2
    -     D:/data/python_projects/W05/src/question_04.py
    - Test case 3
    -     C:/Users/myname/miniconda3/envs/aix/bin
    """

    # ===== Your code here =====
    path = "/".join(list_of_dirs)
    # ==========================

    return path


if __name__ == "__main__":
    print("Test case 1")
    list_of_dirs = [
        "C:",
        "Users",
        "myname",
        "Documents"
    ]
    path = path_join(list_of_dirs)
    print(f"\t{path}") # \t는 space 네 칸(칸수는 다를 수 있음) 띄우기 입니다.

    print("Test case 2")
    list_of_dirs = [
        "D:",
        "data",
        "python_projects",
        "W05",
        "src",
        "question_04.py"
    ]
    path = path_join(list_of_dirs)
    print(f"\t{path}") 

    print("Test case 3")
    list_of_dirs = [
        "C:",
        "Users",
        "myname",
        "miniconda3",
        "envs",
        "aix",
        "bin",
    ]
    path = path_join(list_of_dirs)
    print(f"\t{path}") 

