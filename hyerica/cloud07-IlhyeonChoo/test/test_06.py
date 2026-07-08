import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_06 import preprocess_data


def test_solution():
    data_list = [
        ("data/a/a1.png", "dog"),
        ("data/a/a2.png", "cat"),
        ("data/a/a3.png", "tiger"),
        ("data/a/a4.png", "dog"),
    ]
    preprocessed_data_list = preprocess_data(data_list)
    assert len(preprocessed_data_list) == 4
    assert len(list(filter(lambda t: not t[0].endswith(".png"), preprocessed_data_list))) == 0
    
    data_list = [
        ("data/b/b1.png", "dog"),
        ("data/b/b2.png", "cat"),
        ("data/b/b3.jpg", "tiger"),
        ("data/b/b4.jpg", "dog"),
    ]
    preprocessed_data_list = preprocess_data(data_list)
    assert len(preprocessed_data_list) == 2
    assert len(list(filter(lambda t: not t[0].endswith(".png"), preprocessed_data_list))) == 0
    
    data_list = [
        ("data/c/c1.jpg", "dog"),
        ("data/c/c2.png", "cat"),
        ("data/c/c3.png", "tiger"),
        ("data/c/c4.jpeg", "dog"),
    ]
    preprocessed_data_list = preprocess_data(data_list)
    assert len(preprocessed_data_list) == 2
    assert len(list(filter(lambda t: not t[0].endswith(".png"), preprocessed_data_list))) == 0
    
    data_list = [
        ("data/d/d1.jpg", "dog"),
        ("data/d/d2.png", "cat"),
        ("data/d/d3.png", "tiger"),
        ("data/d/d4.jpeg", "dog"),
        ("data/d/d5.png", "dog"),
        ("data/d/d6.png", "rabbit"),
    ]
    preprocessed_data_list = preprocess_data(data_list)
    assert len(preprocessed_data_list) == 4
    assert len(list(filter(lambda t: not t[0].endswith(".png"), preprocessed_data_list))) == 0
    
    data_list = [
        ("data/e/e1.jpg", "dog"),
        ("data/e/e2.png", "cat"),
        ("data/e/e3.gif", "tiger"),
        ("data/e/e4.jpeg", "dog"),
        ("data/e/e5.png", "tiger"),
        ("data/e/e6.png", "dog"),
    ]
    preprocessed_data_list = preprocess_data(data_list)
    assert len(preprocessed_data_list) == 3
    assert len(list(filter(lambda t: not t[0].endswith(".png"), preprocessed_data_list))) == 0


