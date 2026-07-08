from collections import defaultdict

def build_inverted_index(docs):
    """
    문서 목록(docs)으로부터 역인덱스(inverted index)를 구축하는 함수이다.
    각 단어가 몇 번째 문서(0-based index)에 등장하는지를 기록하시오.
    동일한 단어가 한 문서에 여러 번 등장해도 해당 문서 번호는 한 번만 기록한다.
    (힌트: defaultdict(list) 사용, 각 단어를 키로, 등장 문서 번호 리스트를 값으로)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      docs: 각 원소가 공백으로 구분된 단어들의 문자열인 리스트
    인자:
      docs (list): 각 원소가 문서 문자열인 리스트
    반환값:
      defaultdict: {단어: [등장 문서 번호 리스트]} 형태의 defaultdict(list)
    예시:
      >>> build_inverted_index(["cat dog", "dog bird", "cat bird cat"])
          defaultdict(<class 'list'>, {'cat': [0, 2], 'dog': [0, 1], 'bird': [1, 2]})
    """
    # ===== Your Code Here =====
    inverted_index = defaultdict(list)
    for index, doc in enumerate(docs):
        for word in set(doc.split()):
            inverted_index[word].append(index)
    return inverted_index
    # ==========================

if __name__ == '__main__':
    docs = ["cat dog", "dog bird", "cat bird cat"]
    #### 함수 호출 ####
    index = build_inverted_index(docs)
    print(f'역인덱스: {dict(index)}')
    #################
