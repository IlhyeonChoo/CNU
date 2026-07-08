import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_04 import path_join

def test_path_join():
    list_of_dirs = [
        "C:",
        "Users",
        "myname",
        "Documents"
    ]
    path = path_join(list_of_dirs)
    assert path == "C:/Users/myname/Documents"

    list_of_dirs = [
        "D:",
        "data",
        "python_projects",
        "W05",
        "src",
        "question_04.py"
    ]
    path = path_join(list_of_dirs)
    assert path == "D:/data/python_projects/W05/src/question_04.py"

    list_of_dirs = [
        "C:",
        "Users",
        "myname",
        "miniconda3",
        "envs",
        "aix",
        "bin",
    ]
    path = path_join(list_of_dirs)
    assert path == "C:/Users/myname/miniconda3/envs/aix/bin"

    list_of_dirs = [
        "C:",
        "Users",
        "myname",
        "projects",
        "my_first_project",
        "README.md",
    ]
    path = path_join(list_of_dirs)
    assert path == "C:/Users/myname/projects/my_first_project/README.md"

    list_of_dirs = [
        "C:",
        "Users",
        "myname",
        "projects",
        "my_second_project",
        "test.cpp",
    ]
    path = path_join(list_of_dirs)
    assert path == "C:/Users/myname/projects/my_second_project/test.cpp"
