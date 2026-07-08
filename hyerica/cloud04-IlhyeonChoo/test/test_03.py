import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_03 import tokenize

def test_tokenize():
    tokenized = tokenize("a neural network is a model inspired by the structure and function of animal brains")
    assert len(tokenized) == 15 and tokenized[0] == "a"

    tokenized = tokenize("machine learning can learn from data and generalize to unseen data")
    assert len(tokenized) == 11 and tokenized[-1] == "data"

    tokenized = tokenize("computer vision tasks include methods for processing and understanding digital images")
    assert len(tokenized) == 11 and tokenized[2] == "tasks"
