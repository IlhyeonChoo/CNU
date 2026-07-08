from collections import Counter

def count_frequent_words(sentence, min_count):
    """
    공백으로 구분된 문장(sentence)에서 각 단어의 등장 횟수를 세고,
    min_count번 이상 등장한 단어만 딕셔너리 형태로 반환하는 함수이다.
    (힌트: Counter를 사용하여 단어를 세고, 조건에 맞는 항목만 필터링하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      sentence: 공백으로 구분된 단어들의 문자열
      min_count: 포함 기준이 되는 최소 등장 횟수
    인자:
      sentence (str): 공백으로 구분된 단어들의 문자열
      min_count (int): 최소 등장 횟수 기준 (해당 횟수 이상인 단어만 반환)
    반환값:
      dict: {단어: 등장횟수} 형태의 딕셔너리 (min_count 이상인 단어만 포함)
    예시:
      >>> count_frequent_words("apple banana apple cherry banana apple", 2)
          {'apple': 3, 'banana': 2}
      >>> count_frequent_words("cat dog cat cat dog bird", 3)
          {'cat': 3}
    """
    # ===== Your Code Here =====
    word_counts = Counter(sentence.split())
    return {word: count for word, count in word_counts.items() if count >= min_count}
    # ==========================

if __name__ == '__main__':
    S = "apple banana apple cherry banana apple"
    MIN = 2
    #### 함수 호출 ####
    print(f'결과: {count_frequent_words(S, MIN)}')
    #################
