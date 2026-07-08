def modify_list():
    """
    주어진 리스트(my_list)에서, "Java"에 해당하는 원소를 "Python"으로 바꾸고, "static"에 해당하는 원소를 "dynamic"으로 바꾸세요.
    함수를 완성하신 후, visual studio code 우상단의 실행버튼을 클릭하여 이 파일을 실행(run)해보세요.
    정답출력: "My favorite programming language is Python . It has a dynamic type-checking system ."

    코드작성방법:
    - 코드에서 "None"을 지우고 적절한 코드를 완성하세요.
    - 여기 작성하는 모든 코드는 들여쓰기가 동일하게 되어 있어야 합니다. (space 4개)
    - "이 부분의 코드를 완성하세요" 로 표시된 부분에만 코드를 작성해주세요.

    힌트:
    - my_list[?] = ?

    파라미터:
    - 없음

    반환:
    - my_list: 문자열 리스트
    """

    my_list = ["My", "favorite", "programming", "language", "is", "Java", ".", 
               "It", "has", "a", "static", "type-checking", "system", "."]

    ##### 이 부분의 코드를 완성하세요 #####
    for index in range(len(my_list)):
        if my_list[index] == "Java":
            my_list[index] = "Python"
        if my_list[index] == "static":
            my_list[index] = "dynamic"
    ################################

    return my_list


if __name__ == "__main__":
    # "My favorite programming language is Python . It has a dynamic type-checking system ." 가 출력되어야 함
    print("결과:", " ".join(modify_list()))
