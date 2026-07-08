import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_16 import *

def test():
    b = Book('Python Programming', 123)
    b.borrow()
    assert b.title == 'Python Programming'
    assert b.item_id == 123