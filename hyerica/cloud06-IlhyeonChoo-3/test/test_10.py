import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_10 import solution


def test_solution():
    words = ['python', 'is', 'a', 'high', 'level', 'general', 'purpose', 
             'programming', 'language', 'the', 'design', 'philosophy', 'of', 'python',
             'emphasizes', 'code', 'readability', 'with', 'the', 'use', 'of', 
             'significant', 'indentation', "python", "is" 'dynamically', 'type', 'checked', 
             'and', 'garbage', 'collected']
    word_count = solution(words)
    assert_equal_dict(word_count, {'python': 3, 'is': 1, 'a': 1, 'high': 1, 'level': 1, 'general': 1, 
       'purpose': 1, 'programming': 1, 'language': 1, 'the': 2, 'design': 1, 
       'philosophy': 1, 'of': 2, 'emphasizes': 1, 'code': 1, 'readability': 1, 
       'with': 1, 'use': 1, 'significant': 1, 'indentation': 1, 'isdynamically': 1, 
       'type': 1, 'checked': 1, 'and': 1, 'garbage': 1, 'collected': 1})

    words = ['C++', 'was', 'designed', 'with', 'systems', 'programming', 'and', 'embedded', 
             'resource', 'constrained', 'software', 'and', 'large', 'systems', 'in', 'mind',
             'with', 'performance', 'efficiency', 'and', 'flexibility', 'of', 'use', 'as', 'its',
             'design', 'highlights', 'C++', 'has', 'also', 'been', 'found', 'useful', 'in', 'many', 
             'other', 'contexts', 'with', 'key', 'strengths', 'being', 'software', 'infrastructure',
             'and', 'resource', 'constrained', 'applications', 'performance', 'critical', 'applications']

    word_count = solution(words)
    assert_equal_dict(word_count, {'C++': 2, 'was': 1, 'designed': 1, 'with': 3, 'systems': 2, 'programming': 1, 
       'and': 4, 'embedded': 1, 'resource': 2, 'constrained': 2, 'software': 2, 'large': 1, 
       'in': 2, 'mind': 1, 'performance': 2, 'efficiency': 1, 'flexibility': 1, 'of': 1, 
       'use': 1, 'as': 1, 'its': 1, 'design': 1, 'highlights': 1, 'has': 1, 'also': 1, 
       'been': 1, 'found': 1, 'useful': 1, 'many': 1, 'other': 1, 'contexts': 1, 'key': 1, 
       'strengths': 1, 'being': 1, 'infrastructure': 1, 'applications': 2, 'critical': 1})

    words = ['Java', 'is', 'a', 'highlevel', 'general', 'purpose', 'memory', 'safe', 'object', 'oriented',
             'programming', 'language', 'It', 'is', 'intended', 'to', 'let', 'programmers', 'write',
             'once', 'run', 'anywhere', 'WORA', 'meaning', 'that', 'compiled', 'Java', 'code',
             'can', 'run', 'on', 'all', 'platforms', 'that', 'support', 'Java', 'without', 'the', 'need',
             'to', 'recompile', 'Java', 'applications', 'are', 'typically', 'compiled', 'to', 'bytecode',
             'that', 'can', 'run', 'on', 'any', 'Java', 'virtual', 'machine', 'JVM', 'regardless', 'of',
             'the', 'underlying', 'computer', 'architecture']

    word_count = solution(words)
    assert_equal_dict(word_count, {'Java': 5, 'is': 2, 'a': 1, 'highlevel': 1, 'general': 1, 'purpose': 1, 'memory': 1,
                                   'safe': 1, 'object': 1, 'oriented': 1, 'programming': 1, 'language': 1, 'It': 1,
                                   'intended': 1, 'to': 3, 'let': 1, 'programmers': 1, 'write': 1, 'once': 1, 'run': 3,
                                   'anywhere': 1, 'WORA': 1, 'meaning': 1, 'that': 3, 'compiled': 2, 'code': 1, 'can': 2,
                                   'on': 2, 'all': 1, 'platforms': 1, 'support': 1, 'without': 1, 'the': 2, 'need': 1,
                                   'recompile': 1, 'applications': 1, 'are': 1, 'typically': 1, 'bytecode': 1, 'any': 1,
                                   'virtual': 1, 'machine': 1, 'JVM': 1, 'regardless': 1, 'of': 1, 'underlying': 1,
                                   'computer': 1, 'architecture': 1})


def assert_equal_dict(a, b):
    assert len(a.keys()) == len(b.keys())
    for key in a.keys():
        assert key in b.keys()
        assert a[key] == b[key]

