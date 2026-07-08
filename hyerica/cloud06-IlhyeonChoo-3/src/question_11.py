def solution(name, students):
    """
    **문제**
    딕셔너리(students)가 주어졌을 때, 특정 학생의 이름(name)을 함수의 인자로 전달받아 해당 학생의 점수를 조회하세요.
    만약 해당 이름이 존재하지 않는다면, 점수는 "찾을 수 없음"으로 처리하세요.
    반환 값은 (이름, 점수)의 튜플 형태여야 합니다.

    **출력 예시**
    - 입력 이름: Alice → 출력: (Alice, 85)
    - 입력 이름: David → 출력: (David, 찾을 수 없음)

    **힌트**
    - 딕셔너리의 메서드를 활용하면 기본값을 설정할 수 있습니다.

    **주의**
    - 이름은 대소문자를 구분합니다.
    - 중복된 이름은 없습니다.
    - input()은 main에서 받아 처리되며, 함수에서는 단순히 전달받은 값을 사용합니다.
    """
    # ===== Your code here =====
    score = students.get(name, "찾을 수 없음")

    # ==========================
    
    return name, score
    
if __name__ == "__main__":
    my_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    target = input("찾을 학생의 이름을 입력하세요: ")
    answer = solution(target, my_dict)
    print(answer)
