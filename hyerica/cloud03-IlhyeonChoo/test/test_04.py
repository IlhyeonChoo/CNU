import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_04 import create_dictionary

def test_dictionary_creation():
    one_time_test("Name", "John", "Age", "25")
    one_time_test("Lang1", "Python", "Lang2", "C")
    one_time_test("int", "32bits", "long", "64bits")
    one_time_test("Title", "Harry potter", "Author", "J.K.Rowling")
    one_time_test("Year", "2025", "Month", "March")


def one_time_test(first_key, first_value, second_key, second_value):
    STDOUT = os.path.join(REPOSITORY_ROOT_PATH, "resources", "stdout.txt")

    if os.path.exists(STDOUT):
        os.remove(STDOUT)

    with open(STDOUT, "w") as sys.stdout:
        my_dict = create_dictionary(first_key, first_value, second_key, second_value)
    with open(STDOUT, "r") as f:
        out = f.read()

    os.remove(STDOUT)

    assert out.strip() == first_value
    assert my_dict[first_key] == first_value
    assert my_dict[second_key] == second_value