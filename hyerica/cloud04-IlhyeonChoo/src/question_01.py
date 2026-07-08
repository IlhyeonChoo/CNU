def capitalize(sentence):
    """
    **문제**
    - 문자열의 메소드인 capitalize를 구현하세요. capitalize 메서드를 사용하면 안됩니다.
    - 영소문자로만 이루어진 문장에서, 맨 앞 단어의 첫 문자를 대문자로 바꾸는 코드를 작성하세요.
    - 문장은 sentence라는 변수로 주어집니다.
    - sentence는 영단어 이외에 다른 문자(특수문자, 숫자, 다른 언어 등)를 포함하지 않습니다.
    - sentence에 저장된 문장의 양 끝은 공백이 아닙니다.
    - 프로그래밍을 연습하는 좋은 방법 중 하나가, 프로그래밍 언어에서 기본으로 제공되는 메서드/함수들을 직접 구현해보는 것입니다. 
      파이썬에서 기본으로 제공되는 함수들을 직접 구현하는 연습도 해보시길 바랍니다.
    
    **힌트**
    - 다음 두 문자열의 합으로 구현 가능합니다.
    - {sentence의 첫 문자를 대문자로 바꾼 것} + {sentence의 두 번째 문자부터 마지막 문자까지 (slicing 활용: sentence[?:?])}

    **예상출력**
    - Test case 1
    -     I like dogs
    - Test case 2
    -     A neural network is a model inspired by the structure and function of animal brains
    - Test case 3
    -     Machine learning can learn from data and generalize to unseen data
    - (Test case 3 은 그대로 출력)
    """

    capitalized_sentence = None
    if sentence[0].islower(): # 첫 번째 문자가 소문자인 경우 True
        # ===== Your code here =====
        first_sentence = sentence[0].upper()
        second_sentence = sentence[1:]
        capitalized_sentence = first_sentence + second_sentence
        # ==========================
    else:
        capitalized_sentence = sentence

    return capitalized_sentence


if __name__ == "__main__":
    print("Test case 1")
    capitalized_sentence = capitalize("i like dogs")
    print(f"\t{capitalized_sentence}")

    print("Test case 2")
    capitalized_sentence = capitalize("a neural network is a model inspired by the structure and function of animal brains")
    print(f"\t{capitalized_sentence}")

    print("Test case 3")
    capitalized_sentence = capitalize("Machine learning can learn from data and generalize to unseen data")
    print(f"\t{capitalized_sentence}")
