import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_06 import is_palindrome

def test():
    # 홀수 길이 회문
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("level") == True
    assert is_palindrome("noon") == True  # 짝수 길이 회문

    # 짝수 길이 회문
    assert is_palindrome("abba") == True
    assert is_palindrome("abccba") == True

    # 단일 문자 → 항상 회문
    assert is_palindrome("a") == True
    assert is_palindrome("z") == True

    # 두 문자 회문
    assert is_palindrome("aa") == True
    assert is_palindrome("ab") == False

    # 회문이 아닌 경우
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("abc") == False
    assert is_palindrome("world") == False

    # 숫자 문자열
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
    assert is_palindrome("1221") == True
