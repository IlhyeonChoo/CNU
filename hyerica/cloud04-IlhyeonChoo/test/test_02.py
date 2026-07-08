import sys, os
REPOSITORY_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_PATH, "src"))

from question_02 import filter_gary

def test_capitalize():
    fullnames = ["Jordan Henderson", "Nick Powell", "Gary Neville", "Wayne Rooney", "Gary Cahill"]
    filtered_fullnames = filter_gary(fullnames)
    assert len(filtered_fullnames) == 2 and all(name[:4] == "Gary" for name in filtered_fullnames)

    fullnames = ["Gary O'Neil", "Phil Foden", "Jesse Lingard",]
    filtered_fullnames = filter_gary(fullnames)
    assert len(filtered_fullnames) == 1 and all(name[:4] == "Gary" for name in filtered_fullnames)

    fullnames = ["Harry Kane", "Nicky Butt", "Gary Lineker", "Bukayo Saka", "Gary Rowett"]
    filtered_fullnames = filter_gary(fullnames)
    assert len(filtered_fullnames) == 2 and all(name[:4] == "Gary" for name in filtered_fullnames)