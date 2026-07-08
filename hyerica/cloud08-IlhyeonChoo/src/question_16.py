def classify_students(applicants, enrolled):
    """
    수강 신청 학생(applicants)과 실제 등록 학생(enrolled)을 받아,
    세트(set) 메서드를 사용하여 학생 현황을 분석하고 딕셔너리로 반환하는 함수이다.
    연산자(|, -)가 아닌 반드시 메서드(union, difference, issubset)를 사용하시오.
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      applicants: 수강 신청한 학생 이름의 집합
      enrolled: 실제 등록한 학생 이름의 집합
    인자:
      applicants (set): 수강 신청한 학생 이름의 집합
      enrolled (set): 실제 등록한 학생 이름의 집합
    반환값:
      dict: 다음 세 가지 키를 가지는 딕셔너리
            'all'         : 신청자와 등록자를 합친 전체 학생 집합 (union 메서드)
            'not_enrolled': 신청했지만 등록하지 않은 학생 집합 (difference 메서드)
            'is_subset'   : 등록자가 신청자의 부분집합인지 여부 (issubset 메서드, bool)
    예시:
      >>> classify_students({'Alice', 'Bob', 'Charlie'}, {'Alice', 'Charlie'})
          {'all': {'Alice', 'Bob', 'Charlie'}, 'not_enrolled': {'Bob'}, 'is_subset': True}
    """
    # ===== Your Code Here =====
    return {
        'all': applicants.union(enrolled),
        'not_enrolled': applicants.difference(enrolled),
        'is_subset': enrolled.issubset(applicants),
    }
    # ==========================

if __name__ == '__main__':
    applicants = {'Alice', 'Bob', 'Charlie', 'David'}
    enrolled = {'Alice', 'Charlie'}
    #### 함수 호출 ####
    result = classify_students(applicants, enrolled)
    print(f'전체 학생: {result["all"]}')
    print(f'미등록 학생: {result["not_enrolled"]}')
    print(f'등록자가 부분집합인가: {result["is_subset"]}')
    #################
