def solution(string):
    """
    **문제**
    - 주어진 문자열(string)에 대해, 연속으로 반복되는 문자를 압축하여 표현하는 코드를 작성하세요.
    - 압축 방식:
    - 동일한 문자가 연속으로 나오는 경우 -> “문자+반복횟수” 형식으로 작성
    - 문자가 한번만만 나타나는 경우는 “문자1” 형식으로 작성
    - 아래 처럼 결과값이 나오면 성공입니다.
    - 입력: 'aaabbcaad'
    - 결과: 'a3b2c1a2d1'

    **힌트**
    - 문자열을 반복문으로 순회하며 인접한 알파벳을 비교합니다.
    - 현재 문자와 다음 문자가 같으면 count를 증가시킵니다.
    - 현재 문자와 다음 문자가 다르면 count를 초기화 합니다.
    
    **주의**
    - 반환 값은 문자열입니다.
    """
    answer = ""
    count = 1
    # ===== Your code here =====
    if len(string) <= 1:
        return string + "1"

    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            count += 1
        else:
            answer += string[i-1] + str(count)
            count = 1

    answer += string[-1] + str(count)
    # ==========================

    return answer

if __name__ == "__main__":
    string = "aaabbcaad"
    my_answer = solution(string)
    print(my_answer)