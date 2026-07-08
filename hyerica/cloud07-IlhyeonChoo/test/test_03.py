import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_03 import get_topk_students


def test_solution():
    
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
    topk_student_info = get_topk_students(student_info, k=1)
    topk_student_names = set(map(lambda t: t["name"], topk_student_info))
    assert topk_student_names == { "Bob" }
    
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
    topk_student_info = get_topk_students(student_info, k=2)
    topk_student_names = set(map(lambda t: t["name"], topk_student_info))
    assert topk_student_names == { "Brian", "Alice" }
    
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
    topk_student_info = get_topk_students(student_info, k=3)
    topk_student_names = set(map(lambda t: t["name"], topk_student_info))
    assert topk_student_names == { "Bob", "Brian", "Alice" }
    
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
        {
            "name": "Rose",
            "math_score": 66,
        },
        {
            "name": "Daniel",
            "math_score": 98,
        },
    ]
    topk_student_info = get_topk_students(student_info, k=4)
    topk_student_names = set(map(lambda t: t["name"], topk_student_info))
    assert topk_student_names == { "Bob", "Brian", "Alice", "Daniel" }
    
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
        {
            "name": "Rose",
            "math_score": 66,
        },
        {
            "name": "Daniel",
            "math_score": 98,
        },
        {
            "name": "James",
            "math_score": 100,
        },
        {
            "name": "Matthew",
            "math_score": 78,
        },
    ]
    topk_student_info = get_topk_students(student_info, k=2)
    topk_student_names = set(map(lambda t: t["name"], topk_student_info))
    assert topk_student_names == { "Bob", "James" }

