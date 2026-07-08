def solution(matrix):
    """
    **문제**
    n x n 크기의 2D 리스트(matrix)를 90도 시계 방향으로 회전한
    새로운 2D 리스트를 반환하세요.
 
    **예시**
    입력:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    출력:
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
 
    **힌트**
    - 90도 시계 방향 회전 공식: result[j][n-1-i] = matrix[i][j]
    - 또는 두 단계로 나눠서: ① 전치(transpose) → ② 각 행을 뒤집기(reverse)
    - n x n 크기의 0으로 초기화된 2D 리스트를 먼저 만드세요:
        result = [[0] * n for _ in range(n)]
 
    **주의**
    - 원본 matrix를 직접 수정하지 말고 새 리스트를 만들어 반환하세요.
    - 리스트/인덱스 이외의 자료구조를 사용하지 마세요.
    """
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
 
    # ===== Your code here =====

    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]

    # ==========================
    return result
 
 
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    answer = solution(matrix)

    for row in answer:
        print(" ", row)
