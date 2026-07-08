def solution(target, typed):
    """
    **문제**
    주어진 두 문자열(target, typed)을 비교하여 다음과 같은 정보를 반환하는 코드를 작성하세요.
    - 정확하게 입력된 글자 수
    - 오타 개수
    - 첫 번째 오타의 위치 (0부터 시작, 공백은 무시한 위치)

    단, 공백(" ")은 무시하고 비교하며, 두 문자열의 길이는 같다고 가정합니다.

    **예시**
    입력: target = "hello world", typed = "hezlo wprld"
    출력: [8, 2, 2] (correct, mistakes, first_mistake)

    **힌트**
    - zip()을 함께 사용하면 유용합니다.
    - 공백이 아닌 문자만 비교하세요.
    - 오타 발생 시 해당 위치를 기록하세요.

    **주의**
    - 함수 내부에서는 외부 전역 변수(text 등)를 직접 사용하지 마세요.
    """
    correct = 0
    mistakes = 0
    first_mistake = -1
    idx = 0  # 공백 무시한 비교 인덱스
    
    # ===== Your code here =====
    for target_char, typed_char in zip(target, typed):
        if target_char == " ":
            continue

        if target_char == typed_char:
            correct += 1
        else:
            mistakes += 1
            if first_mistake == -1:
                first_mistake = idx

        idx += 1

    # ==========================

    return [correct, mistakes, first_mistake]
    
if __name__ == "__main__":
    text = "hello world"
    my_text = "hezlo wprld"
    answer = solution(text, my_text)
    print(f"{answer[0]}글자 정확 / {answer[1]}개 오타 / 첫 오타 위치: {answer[2]}")
