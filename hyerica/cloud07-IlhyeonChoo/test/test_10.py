import os, sys, random
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_10 import path_join


def test_solution():
    assert path_join("D:", "data", "mydata.txt").strip() == "D:/data/mydata.txt"
    assert path_join("D:", "data", "extra", "mydata.txt").strip() == "D:/data/extra/mydata.txt"
    assert path_join("C:", "drive", "extra", "mydata.txt").strip() == "C:/drive/extra/mydata.txt"
    assert path_join("C:", "drive", "study", "ai_coding.pptx").strip() == "C:/drive/study/ai_coding.pptx"


