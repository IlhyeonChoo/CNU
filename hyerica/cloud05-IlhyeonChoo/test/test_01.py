import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_01 import search

def test_search():
    test_cases = [
        "Probability is a branch of mathematics and statistics concerning events and numerical descriptions of how likely they are to occur".split(" "),
        "The probability of an event is a number between 0 and 1; the larger the probability, the more likely an event is to occur.[note 1][1][2] This number is often expressed as a percentage (%), ranging from 0% to 100%".split(" "),
        "A simple example is the tossing of a fair (unbiased) coin. Since the coin is fair, the two outcomes ('heads' and 'tails') are both equally probable; the probability of 'heads' equals the probability of 'tails'; and since no other outcomes are possible, the probability of either 'heads' or 'tails' is 1/2 (which could also be written as 0.5 or 50%)".split(" ")
    ]

    queries = ["branch", "larger", "equally"]

    for tc, q in zip(test_cases, queries):
        assert search(q, tc) == tc.index(q)
