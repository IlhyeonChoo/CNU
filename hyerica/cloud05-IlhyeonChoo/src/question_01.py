def search(query, list_of_string):
    """
    문자열로 구성된 리스트(list_of_string)가 주어지고, 하나의 문자열(query)이 주어졌을 때, query 문자열이 list_of_string 내에 어느 위치에 있는지 찾는 코드를 작성하세요.
    위치는 index 변수에 저장해주시고, 위치는 1부터가 아닌, 0부터 시작하도록 index를 설정하세요.
    예를들어, list_of_string = ["AAA", "B", "CC", "DDDD"] 이고, query = "B" 이면, index = 1 이 되어야 합니다.
    만약, query 문자열이 list_of_string 내에 없으면, index 값은 -1로 설정하세요.

    본 파일을 실행했을때의 예상출력: 
        Python 검색위치: 7
    """

    ##### 이 부분의 코드를 완성하세요 #####
    index = -1

    for i, value in enumerate(list_of_string):
        if value == query:
            index = i
            break

    ################################

    return index    


if __name__ == "__main__":
    programming_languages = ["C++", "C#", "Go", "LISP", "Lua", "Java", "Javascript", "Python", "Scala"]
    print("Python 검색위치:", search("Python", programming_languages))
