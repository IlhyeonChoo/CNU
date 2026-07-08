import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_16 import classify_students

def test():
    # 기본 케이스: 등록자가 신청자의 부분집합
    applicants = {'Alice', 'Bob', 'Charlie', 'David'}
    enrolled = {'Alice', 'Charlie'}
    result = classify_students(applicants, enrolled)
    assert result['all'] == {'Alice', 'Bob', 'Charlie', 'David'}
    assert result['not_enrolled'] == {'Bob', 'David'}
    assert result['is_subset'] == True

    # 등록자가 신청자보다 많은 경우 (is_subset = False)
    applicants2 = {'A', 'B'}
    enrolled2 = {'A', 'B', 'C'}
    result2 = classify_students(applicants2, enrolled2)
    assert result2['all'] == {'A', 'B', 'C'}
    assert result2['not_enrolled'] == set()
    assert result2['is_subset'] == False

    # 모두 등록한 경우 → not_enrolled 공집합
    applicants3 = {'X', 'Y', 'Z'}
    enrolled3 = {'X', 'Y', 'Z'}
    result3 = classify_students(applicants3, enrolled3)
    assert result3['not_enrolled'] == set()
    assert result3['is_subset'] == True

    # 신청자와 등록자가 완전히 다른 경우
    applicants4 = {'P', 'Q'}
    enrolled4 = {'R', 'S'}
    result4 = classify_students(applicants4, enrolled4)
    assert result4['all'] == {'P', 'Q', 'R', 'S'}
    assert result4['not_enrolled'] == {'P', 'Q'}
    assert result4['is_subset'] == False

    # 등록자가 1명인 경우
    applicants5 = {'Tom', 'Jerry', 'Spike'}
    enrolled5 = {'Tom'}
    result5 = classify_students(applicants5, enrolled5)
    assert result5['not_enrolled'] == {'Jerry', 'Spike'}
    assert result5['is_subset'] == True

    # 반환 딕셔너리 키 확인
    r = classify_students({'a'}, {'a'})
    assert 'all' in r
    assert 'not_enrolled' in r
    assert 'is_subset' in r
