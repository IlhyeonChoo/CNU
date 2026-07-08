import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_02 import get_words


def test_solution():
    my_sentence = "In computer programming, a variable is an abstract storage location paired with an associated symbolic name"
    assert get_words(my_sentence) == ['a', 'an', 'abstract', 'an', 'associated']

    my_sentence = "Variables in programming may not directly correspond to the concept of variables in mathematics"
    assert [] == get_words(my_sentence)

    my_sentence = "Depending on the type system of a programming language, variables may only be able to store a specified data type"
    assert ['a', 'able', 'a'] == get_words(my_sentence)


