def tokenize(sentence):
    """
    **문제**
    - 주어진 문장으로부터 단어들의 리스트를 구하는 코드를 작성하세요.
    - 문장은 sentence 라는 변수로 주어집니다.
    - sentence는 영소문자로만 구성된 문장이며, 문장을 space 1칸 단위로 자르면 단어들의 리스트가 됩니다.
    - sentence에는 특수문자가 포함되지 않습니다.
    - 단어의 복수형을 단수형으로 바꾼다거나, 동사를 모두 동사원형 형태로 만드는 건 하지 않으셔도 됩니다. (space 1칸 단위로 자르기만 하세요)
    - 이 작업은 "tokenization"라고 불리며, 컴퓨터에서 인간의 언어를 처리할때 필수적으로 사용되는 개념입니다.
      ChatGPT와 같은 인공지능 챗봇이 인간으로부터 질의를 받았을때 맨 처음 수행되는 과정이 tokenization 이도 합니다.
      (실제로는 특수문자 따위도 처리해야해서 여기서 구현한것보다 복잡한 알고리즘을 사용합니다)

    **힌트**
    - 문자열의 .split 메서드 활용
    - split() 메서드의 입력으로는 문자열을 자른 구분자가 들어갑니다.
    -   예 1: 구분자가 문자 1개인 경우
    -       my_string = "aaa!bbb!ccc"
    -       print(my_string.split("!")) # ["aaa", "bbb", "ccc"]
    -   예 2: 구분자가 문자열인 경우
    -       my_string = "aaa! ^bbb! ^))ccc"
    -       print(my_string.split("! ^")) # ["aaa", "bbb", "))ccc"]

    **예상출력**
    - Test case 1
    -     ["we", "are", "university", "students"]
    - Test case 2
    -     ["a", "cute", "dog"]
    - Test case 3
    -     ["i", "like", "hamburgers"]
    """

    # ===== Your code here =====
    # sentence의 split 메서드를 호출하세요.
    # None 을 지우고 작성하세요.
    list_of_words = sentence.split(" ")
    # ==========================

    return list_of_words


if __name__ == "__main__":
    print("Test case 1")
    list_of_words = tokenize("we are university students")
    print(f"\t{list_of_words}") # \t는 space 네 칸(칸수는 다를 수 있음) 띄우기 입니다.

    print("Test case 2")
    list_of_words = tokenize("a cute dog")
    print(f"\t{list_of_words}")

    print("Test case 3")
    list_of_words = tokenize("i like hamburgers")
    print(f"\t{list_of_words}")