def solution(candidates):
    """
    **문제**
    - 채용 후보자들의 지원서(candidates)가 주어졌을때, Python 경험이 있고, 3년 이상 경력이 있으며, github 활동 경험이 있는 지원자의 이름만 필터링한 리스트를 반환하세요.
    - 단, list comprehension을 사용하여 한 줄의 코드로 작성하세요.
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 결과: ['Alice', 'Charlie']

    **힌트**
    - list comprehension은 리스트 내부에서 반복문과 조건문을 사용할 수 있습니다.
    - skills에서 'Python'이 포함되어 있는지 확인합니다.
    - experience(경력)가 3년 이상인지 확인합니다.
    - github 활동 경험이 True인지 확인합니다.
    - 3개의 조건을 모두 만족하는 지원자의 이름을 리스트에 담아 반환합니다.

    **주의**
    - return None에서 None을 수정하여 결과를 반환하세요.
    """
    # ===== Your code here =====
    result = [candidate["name"] for candidate in candidates if "Python" in candidate["skills"] and candidate["experience"] >= 3 and candidate["github"]]

    # ==========================
    
    return result

if __name__ == "__main__":
    candidates = [{"name": "Alice", "skills": ["Python", "C++"], "experience": 5, "github": True},
                {"name": "Bob", "skills": ["Java", "Python"], "experience": 2, "github": False},
                {"name": "Charlie", "skills": ["Python", "JavaScript"], "experience": 4, "github": True},]
    my_answer = solution(candidates)
    print(my_answer)