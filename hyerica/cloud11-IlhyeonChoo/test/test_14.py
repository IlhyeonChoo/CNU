import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))
import numpy as np
from PIL import Image

from question_14 import cosine_similarity_to_query


def test():
    vectors = np.array([[1, 0], [0, 1], [1, 1]])
    query = np.array([1, 1])
    result = cosine_similarity_to_query(vectors, query)
    assert np.sum(result) == 2.414213562373095

