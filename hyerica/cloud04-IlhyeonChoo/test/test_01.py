import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_01 import capitalize

def test_capitalize():
    capitalized_sentence = capitalize("i like dogs")
    assert capitalized_sentence[0].isupper()

    capitalized_sentence = capitalize("a neural network is a model inspired by the structure and function of animal brains")
    assert capitalized_sentence[0].isupper()

    capitalized_sentence = capitalize("machine learning can learn from data and generalize to unseen data")
    assert capitalized_sentence[0].isupper()

    capitalized_sentence = capitalize("computer vision tasks include methods for processing and understanding digital images")
    assert capitalized_sentence[0].isupper()

    capitalized_sentence = capitalize("this is a test code")
    assert capitalized_sentence[0].isupper()