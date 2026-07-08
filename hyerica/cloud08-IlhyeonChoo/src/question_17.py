def build_tag_dict(items):
    """
    (태그 집합, 설명) 쌍의 리스트(items)를 받아,
    태그 집합을 키로, 설명을 값으로 하는 딕셔너리를 생성하여 반환하는 함수이다.
    일반 set은 변경 가능(mutable)하여 딕셔너리 키로 사용할 수 없으므로,
    변경 불가능한(immutable) frozenset으로 변환하여 키로 사용하시오.
    (힌트: frozenset(tags) 로 변환하시오)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      items: (태그_집합, 설명_문자열) 튜플의 리스트
    인자:
      items (list): (set, str) 튜플의 리스트. 각 원소는 (태그 집합, 설명 문자열)
    반환값:
      dict: {frozenset(태그들): 설명문자열} 형태의 딕셔너리
    예시:
      >>> build_tag_dict([({'python', 'beginner'}, 'Intro to Python'),
      ...                 ({'data', 'pandas'}, 'Data Analysis')])
          {frozenset({'python', 'beginner'}): 'Intro to Python',
           frozenset({'data', 'pandas'}): 'Data Analysis'}
    """
    # ===== Your Code Here =====
    return {frozenset(tags): description for tags, description in items}
    # ==========================

if __name__ == '__main__':
    items = [
        ({'python', 'beginner'}, 'Intro to Python'),
        ({'data', 'pandas'}, 'Data Analysis'),
        ({'python', 'advanced'}, 'Advanced Python'),
    ]
    #### 함수 호출 ####
    tag_dict = build_tag_dict(items)
    for key, val in tag_dict.items():
        print(f'{set(key)}: {val}')
    #################
