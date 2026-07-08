def solution(list_of_words):
    """
    **문제**
    - 단어들의 리스트 list_of_words로부터 각 단어들의 빈도수를 딕셔너리 형태로 저장한 word_count를 구하는 코드를 작성하세요.
    - 이전 실습에서 보았던 word count와 결과물은 같지만, 이번에는 딕셔너리의 'get' 메서드를 이용해서 구현해보세요.
    - list_of_words 속 단어들을 순회하면서, word_count 내에 해당 단어가 있으면 빈도수를 얻어오고, 그렇지 않으면 0을 얻어오도록, 'get'을 이용하여 구현해보세요.
    - 이전과 마찬가지로, list_of_words은 단어들의 리스트로 주어집니다 (예: ["an" "apple", ...]).
    - 단어들의 빈도수는 딕셔너리 형태로 구현해야 하며, 단어를 키로, 빈도수를 값으로 저장하면 됩니다.
      예: list_of_words에서, "an"이 4번 나오고 "apple"이 2번 나왔으면, word_count = {"an": 4, "apple": 2, ...}

    **힌트**
    - word_count 딕셔너리의 .get 메서드를 활용하세요.
    - dictionary라는 이름의 딕셔너리가 있을때, result = dictionary.get(key, "unknown")은 다음과 같은 효과를 가짐
    - result = None
    - if key in dictionary.keys():
    -     result = dictionary[key]
    - else:
    -     result = "unknown"
    
    **예상출력**
    - {'python': 3, 'is': 1, 'a': 1, 'high': 1, 'level': 1, 'general': 1, 
       'purpose': 1, 'programming': 1, 'language': 1, 'the': 2, 'design': 1, 
       'philosophy': 1, 'of': 2, 'emphasizes': 1, 'code': 1, 'readability': 1, 
       'with': 1, 'use': 1, 'significant': 1, 'indentation': 1, 'isdynamically': 1, 
       'type': 1, 'checked': 1, 'and': 1, 'garbage': 1, 'collected': 1}

    - {'C++': 2, 'was': 1, 'designed': 1, 'with': 3, 'systems': 2, 'programming': 1, 
       'and': 4, 'embedded': 1, 'resource': 2, 'constrained': 2, 'software': 2, 'large': 1, 
       'in': 2, 'mind': 1, 'performance': 2, 'efficiency': 1, 'flexibility': 1, 'of': 1, 
       'use': 1, 'as': 1, 'its': 1, 'design': 1, 'highlights': 1, 'has': 1, 'also': 1, 
       'been': 1, 'found': 1, 'useful': 1, 'many': 1, 'other': 1, 'contexts': 1, 'key': 1, 
       'strengths': 1, 'being': 1, 'infrastructure': 1, 'applications': 2, 'critical': 1}
    """

    word_count = {}

    for word in list_of_words:
        # ===== Your code here =====
        # .get 메서드 활용: word가 word_count에 있으면 그 값을 얻어오고, 없으면 0 얻어오도록
        frequency = word_count.get(word, 0)
        # ==========================
        word_count[word] = frequency + 1

    return word_count


if __name__ == "__main__":
    words = ['python', 'is', 'a', 'high', 'level', 'general', 'purpose', 
             'programming', 'language', 'the', 'design', 'philosophy', 'of', 'python',
             'emphasizes', 'code', 'readability', 'with', 'the', 'use', 'of', 
             'significant', 'indentation', "python", "is" 'dynamically', 'type', 'checked', 
             'and', 'garbage', 'collected']
    word_count = solution(words)
    print(word_count)

    words = ['C++', 'was', 'designed', 'with', 'systems', 'programming', 'and', 'embedded', 
             'resource', 'constrained', 'software', 'and', 'large', 'systems', 'in', 'mind',
             'with', 'performance', 'efficiency', 'and', 'flexibility', 'of', 'use', 'as', 'its',
             'design', 'highlights', 'C++', 'has', 'also', 'been', 'found', 'useful', 'in', 'many', 
             'other', 'contexts', 'with', 'key', 'strengths', 'being', 'software', 'infrastructure',
             'and', 'resource', 'constrained', 'applications', 'performance', 'critical', 'applications']

    word_count = solution(words)
    print(word_count)

