from collections import Counter

def common_words_total_count(text1, text2):
    """
    두 텍스트(text1, text2)에서 공통으로 등장하는 단어를 찾고,
    해당 공통 단어들의 두 텍스트 전체 합산 등장 횟수를 Counter로 반환하는 함수이다.
    1. 각 텍스트를 공백으로 분리하여 Counter를 만든다.
    2. 두 Counter의 교집합(&)으로 공통 단어 집합을 구한다.
    3. 공통 단어에 대해 두 Counter의 합산(+)에서 해당 단어 횟수를 구해 반환한다.
    (힌트: (c1 + c2)로 두 Counter를 합산하고, 공통 단어만 필터링하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      text1: 첫 번째 텍스트 문자열
      text2: 두 번째 텍스트 문자열
    인자:
      text1 (str): 공백으로 구분된 단어들의 첫 번째 문자열
      text2 (str): 공백으로 구분된 단어들의 두 번째 문자열
    반환값:
      Counter: 공통 단어의 두 텍스트 합산 등장 횟수를 나타내는 Counter 객체
    예시:
      >>> common_words_total_count("cat dog cat", "dog bird dog")
          Counter({'dog': 3})
          # 'dog': text1에서 1번 + text2에서 2번 = 3번
          # 'cat'은 text2에 없으므로 제외
          # 'bird'는 text1에 없으므로 제외
    """
    # ===== Your Code Here =====
    counter1 = Counter(text1.split())
    counter2 = Counter(text2.split())
    common_words = counter1 & counter2
    total_counts = counter1 + counter2
    return Counter({word: total_counts[word] for word in common_words})
    # ==========================

if __name__ == '__main__':
    text1 = "cat dog cat apple"
    text2 = "dog bird dog apple apple"
    #### 함수 호출 ####
    result = common_words_total_count(text1, text2)
    print(f'공통 단어 합산 횟수: {result}')
    #################
