import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_09 import solution


def test_solution():
    person_info = {
        "name": "Alice",
        "age": 29
    }
    person_info = solution(person_info)
    assert len(person_info.keys()) == 3
    assert person_info["adult"] == True

    person_info = {
        "name": "Bob",
        "age": 18
    }
    person_info = solution(person_info)
    assert len(person_info.keys()) == 3
    assert person_info["adult"] == False

    person_info = {
        "name": "Charlie",
        "age": 22
    }
    person_info = solution(person_info)
    assert len(person_info.keys()) == 3
    assert person_info["adult"] == True

    person_info = {
        "name": "Diana",
        "age": 34
    }
    person_info = solution(person_info)
    assert len(person_info.keys()) == 3
    assert person_info["adult"] == True

    person_info = {
        "name": "Eva",
        "age": 12
    }
    person_info = solution(person_info)
    assert len(person_info.keys()) == 3
    assert person_info["adult"] == False


