def solution(sentence):
    """
    **문제**
    주어진 문자열에서 동일한 문자가 연속으로 두 개 짝지어 있는 경우 해당 쌍을 제거합니다.
    이 과정을 반복하여 더 이상 제거할 쌍이 없을 때 남는 문자열을 반환하세요.

    **예시**
    입력: "abbac"
    처리:
      → 'bb' 제거 → "aac"
      → 'aa' 제거 → "c"
    출력: "c"

    **힌트**
    - 스택의 마지막 값과 현재 문자가 같으면 pop, 아니면 append 하세요.
    - 문자열 끝까지 처리한 후, 스택에 남은 문자를 합쳐 반환하면 됩니다.

    **주의**
    - 반드시 pop, append를 활용해 작성하세요.
    - 함수 내부에서는 외부 전역 변수(text 등)를 직접 사용하지 마세요.
    """


    # ===== Your code here =====
    stack = []
    for char in sentence:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # ==========================
    
    return "".join(stack)
    
if __name__ == "__main__":
    text = "abbac"
    answer = solution(text)
    print(answer)
