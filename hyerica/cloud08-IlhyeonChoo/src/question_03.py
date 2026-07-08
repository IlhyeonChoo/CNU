from collections import Counter

def combine_word_counts(docs):
    """
    여러 문서(docs)의 단어 목록을 받아 전체 단어 빈도를 합산하는 함수이다.
    빈 Counter를 만들고 Counter의 update 메서드를 반복 사용하여 모든 문서의 단어를 합산하시오.
    (힌트: total = Counter() 로 시작하고, total.update(Counter(doc)) 를 반복하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      docs: 각 원소가 단어 리스트인 리스트 (리스트의 리스트)
    인자:
      docs (list): 각 원소가 단어 리스트인 리스트
    반환값:
      Counter: 전체 단어 빈도를 나타내는 Counter 객체
    예시:
      >>> combine_word_counts([['cat', 'dog'], ['cat', 'bird'], ['dog', 'dog']])
          Counter({'dog': 3, 'cat': 2, 'bird': 1})
    """
    # ===== Your Code Here =====
    total = Counter()
    for doc in docs:
        total.update(Counter(doc))
    return total
    # ==========================

if __name__ == '__main__':
    docs = [['cat', 'dog'], ['cat', 'bird'], ['dog', 'dog']]
    #### 함수 호출 ####
    print(f'단어 빈도: {combine_word_counts(docs)}')
    #################
