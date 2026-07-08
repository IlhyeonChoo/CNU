import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

import question_05


def test_solution():
    for i in range(10):
        question_05.preprocess_data(f"Data {i}")

    assert question_05.global_counter == 10

    for i in range(10):
        question_05.preprocess_data(f"Data {i}")

    assert question_05.global_counter == 20

    for i in range(30):
        question_05.preprocess_data(f"Data {i}")

    assert question_05.global_counter == 50


