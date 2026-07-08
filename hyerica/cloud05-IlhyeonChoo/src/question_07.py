def solution(nums, k):
    """
    **문제**
    정수 리스트 nums와 윈도우 크기 k가 주어질 때,
    크기 k인 윈도우를 왼쪽에서 오른쪽으로 한 칸씩 슬라이딩하면서
    각 윈도우 내 최댓값을 담은 리스트를 반환하세요.
 
    **예시**
    입력: nums = [3, 1, 5, 2, 8, 4, 6], k = 3
    출력: [5, 5, 8, 8, 8]
      - nums[0..2] = [3, 1, 5] → 5
      - nums[1..3] = [1, 5, 2] → 5
      - nums[2..4] = [5, 2, 8] → 8
      - nums[3..5] = [2, 8, 4] → 8
      - nums[4..6] = [8, 4, 6] → 8
 
    **힌트**
    - 슬라이싱 nums[i:i+k]로 각 윈도우를 추출하세요.
    - 반복 횟수는 len(nums) - k + 1 입니다.
    - 내장 함수 max()를 활용하세요.
 
    **주의**
    - 별도 정렬은 사용하지 마세요.
    - 리스트/인덱스 이외의 자료구조를 사용하지 마세요.
    """
    result = []
 
    # ===== Your code here =====
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        result.append(max(window))

    # ==========================
    return result
 
 
if __name__ == "__main__":
    nums = [3, 1, 5, 2, 8, 4, 6]
    k = 3
    answer = solution(nums, k)
    print(answer)