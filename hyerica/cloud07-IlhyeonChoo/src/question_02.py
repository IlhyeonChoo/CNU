# ----- Your code here -----
def get_words(sentence):
    """
    문장을 단어로 쪼개고(공백기준으로 자르기), 각 단어를 소문자로만 이루어지도록 바꾼 후, a로 시작하는 단어들의 리스트만 추출하는 함수를 작성하세요.
    1. 문장을 단어로 쪼개기
    2. 단어들을 소문자로 바꾸기
    3. a로 시작하는 단어들만 필터링해서 가져오기

    이때, 2번과정은 map, 3번과정은 filter 함수를 이용하세요.

    인자:
    - sentence: 문장 1개 (문자열 형식)

    반환값:
    - filtered_words: a로 시작하는 단어들의 리스트 (각 단어들은 소문자로만 구성되어야 함)
    """

    # 1. 문장을 단어로 쪼개기
    words = sentence.split()

    # 2. 단어들을 소문자로 바꾸기
    lower_words = map(str.lower, words)

    # 3. a로 시작하는 단어들만 필터링해서 가져오기
    filtered_words = list(filter(lambda word: word.startswith("a"), lower_words))

    return filtered_words


# --------------------------


if __name__ == "__main__":
    """
    예상출력:
        ['a', 'an', 'abstract', 'an', 'associated']
        []
        ['a', 'able', 'a']
    """
    
    my_sentence = "In computer programming, a variable is an abstract storage location paired with an associated symbolic name"
    print(get_words(my_sentence))

    my_sentence = "Variables in programming may not directly correspond to the concept of variables in mathematics"
    print(get_words(my_sentence))

    my_sentence = "Depending on the type system of a programming language, variables may only be able to store a specified data type"
    print(get_words(my_sentence))
