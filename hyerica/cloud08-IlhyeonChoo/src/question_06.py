from collections import deque

def is_palindrome(s):
    """
    문자열(s)이 회문(palindrome)인지 확인하는 함수이다.
    deque를 사용하여 양 끝에서 문자를 하나씩 꺼내 비교하는 방식으로 구현하시오.
    (힌트: deque의 popleft()로 왼쪽, pop()으로 오른쪽 문자를 꺼내 비교한다)
    함수에 사용되는 매개변수를 다음과 같이 설정하시오:
      s: 검사할 문자열
    인자:
      s (str): 회문 여부를 확인할 문자열
    반환값:
      bool: 회문이면 True, 아니면 False
    예시:
      >>> is_palindrome("racecar")
          True
      >>> is_palindrome("hello")
          False
      >>> is_palindrome("madam")
          True
    """
    # ===== Your Code Here =====
    chars = deque(s)
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True
    # ==========================

if __name__ == '__main__':
    words = ["racecar", "hello", "madam", "python"]
    #### 함수 호출 ####
    for word in words:
        print(f'"{word}" 회문 여부: {is_palindrome(word)}')
    #################
