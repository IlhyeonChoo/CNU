import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_17 import *

def test():
    s = KoreanRecipe('버섯찌개', ['버섯', '돼지고기', '양파'], 5)
    assert s.name == '버섯찌개'
    assert s.ingredients == ['버섯', '돼지고기', '양파']
    assert s.spice_level == 5