import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_18 import *

def test():
    p = PlayList()
    s1 = Song("A", "AA", 202)
    s2 = Song("B", "BB", 178)
    s3 = Song("C", "CC", 178)
    p.add_song(s1).add_song(s2).add_song(s3)

    assert len(p) == 3
    assert p[1] == s2