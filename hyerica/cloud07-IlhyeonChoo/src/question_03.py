def get_topk_students(student_info_list, k):
    """
    학생의 이름과 수학점수로 이루어진 리스트 student_info_list가 주어졌을 때, 수학점수가 가장 높은 k명의 학생 리스트를 반환하는 함수를 구현하세요.
    sorted 함수와 익명함수를 사용하세요.
    이때, student_info_list는 다음처럼 구성됩니다.
        student_info_list = [
            {"name": "Alice", "math_score": 88},
            {"name": "Bob", "math_score": 76},
            ...
        ]

    인자:
    - student_info_list: 학생정보 딕셔너리의 리스트
    - k: 양의 정수값

    반환값:
    - topk_student_info_list: 수학점수가 가장 높은 k명의 학생정보를 담은 리스트
    """
    

    # ----- Your code here -----
    # sorted 함수를 이용하여 studenet_info_list를 정렬하시오. 이때, sorted 함수에 key 인자를 사용해야 합니다.
    sorted_student_info = sorted(
        student_info_list,
        key=lambda student_info: student_info["math_score"],
        reverse=True,
    )

    # list slicing을 이용하여 마지막 k개의 원소만 가져오세요.
    # 아니면, sorted에서 reverse=True를 주신 후, 첫 k개의 원소만 가져오셔도 됩니다.
    topk_student_info_list = sorted_student_info[:k]
    # --------------------------

    return topk_student_info_list


if __name__ == "__main__":
    """
    예상출력:
        [{'name': 'Bob', 'math_score': 100}]
        [{'name': 'Alice', 'math_score': 88}, {'name': 'Brian', 'math_score': 96}]
        [{'name': 'Alice', 'math_score': 88}, {'name': 'Brian', 'math_score': 97}, {'name': 'Bob', 'math_score': 100}]
    """
    
    student_info = [
        {
            "name": "Alice",
            "math_score": 88,
        },
        {
            "name": "Bob",
            "math_score": 100,
        },
        {
            "name": "Brown",
            "math_score": 68,
        },
    ]
    print(get_topk_students(student_info, k=1))
    
    student_info = [
        {
            "name": "Alice",
            "math_score": 88,
        },
        {
            "name": "Bob",
            "math_score": 38,
        },
        {
            "name": "Brown",
            "math_score": 68,
        },
        {
            "name": "Brian",
            "math_score": 96,
        },
    ]
    print(get_topk_students(student_info, k=2))
    
    student_info = [
        {
            "name": "Alice",
            "math_score": 88,
        },
        {
            "name": "Bob",
            "math_score": 100,
        },
        {
            "name": "Brown",
            "math_score": 68,
        },
        {
            "name": "Brian",
            "math_score": 97,
        },
        {
            "name": "John",
            "math_score": 60,
        },
    ]
    print(get_topk_students(student_info, k=3))
