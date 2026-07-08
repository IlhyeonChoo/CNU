import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_13 import analyze_tags

def test():
    post1_tags = ['python', 'ai', 'data', 'python']
    post2_tags = ['data', 'ml', 'python', 'deeplearning']

    intersection, union, difference = analyze_tags(post1_tags, post2_tags)
    assert 'data' in intersection and 'python' in intersection
    assert 'data' in union and 'ml' in union and 'ai' in union and 'python' in union and 'deeplearning' in union
    assert 'ai' in difference

    