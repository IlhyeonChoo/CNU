def analyze_tags(post1, post2):
    """
    두개의 게시물에 사용된 태그 리스트를 입력 받는 함수이다.
    각 게시물의 태그 리스트를 세트로 변환하여 중복을 제거하고,
    1. 두 게시물에 공통으로 사용된 태그 찾기 (교집합)
    2. 두 게시물에 사용된 모든 고유한 태그 찾기 (합집합)
    3. 첫번째 게시물에만 사용된 태그 찾기 (차집합)
    세가지 결과를 모두 반환하세요.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      post1: 첫번째 게시물의 태그 리스트
      post2: 두번째 게시물의 태그 리스트
    인자:
      post1 (list): 첫번째 게시물의 태그 리스트
      post2 (list): 두번째 게시물의 태그 리스트
    반환값:
      tuple: 교집합(set), 합집합(set), 차집합(set)
    예시:
      >>> analyze_tags(post1_tags, post2_tags)
         ({'data', 'python'}, {'data', 'ml', 'ai', 'python', 'deeplearning'}, {'ai'})
    """
    # ===== Your Code Here =====
    post1_tags = set(post1)
    post2_tags = set(post2)
    intersection = post1_tags & post2_tags
    union = post1_tags | post2_tags
    difference = post1_tags - post2_tags
    # ==========================

    return intersection, union, difference

if __name__ == '__main__':
    post1_tags = ['python', 'ai', 'data', 'python']
    post2_tags = ['data', 'ml', 'python', 'deeplearning']
    #### 함수 호출 ####
    intersection, union, difference = analyze_tags(post1_tags, post2_tags)
    #################

    print(f'공통 태그: {intersection}, 모든 태그: {union}, 첫번째 게시글 태그: {difference}')
