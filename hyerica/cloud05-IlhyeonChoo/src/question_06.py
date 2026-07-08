def solution(matrix):
    """
    **문제**
    n x n 크기의 2D 리스트(matrix)가 주어질 때,
    바깥쪽에서 안쪽으로 나선형(시계 방향) 순서로 읽은 1D 리스트를 반환하세요.
 
    **예시**
    입력:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    출력: [1, 2, 3, 6, 9, 8, 7, 4, 5]
 
    **힌트**
    - top, bottom, left, right 경계를 관리하면서 좁혀 나가세요.
    - 한 방향을 다 읽은 뒤 해당 경계를 한 칸씩 안으로 이동하세요.
    - while 반복과 경계 비교 조건이 핵심입니다.
 
    **주의**
    - 추가 2D 리스트를 새로 만들지 말고 경계 인덱스만으로 해결하세요.
    - 리스트/인덱스 이외의 자료구조(딕셔너리, 튜플 등)를 사용하지 마세요.
    """
    result = []
 
    # ===== Your code here =====
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    # ==========================
    return result
 
 
if __name__ == "__main__":
    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]
    answer = solution(matrix)
    print(answer)
    
