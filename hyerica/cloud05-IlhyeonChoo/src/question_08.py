def solution(nums, target_sum):
    """
    **문제**
    정수 리스트 nums와 정수 target_sum이 주어질 때,
    연속된 부분 리스트(subarray)의 합이 target_sum과 같은
    모든 [시작 인덱스, 끝 인덱스] 쌍을 담은 2D 리스트를 반환하세요.
    (끝 인덱스는 포함)
 
    **예시**
    입력: nums = [1, 2, 3, 1, 4, 2, 3], target_sum = 6
    출력: [[0, 2], [1, 3], [4, 5]]
      - nums[0..2] = 1+2+3 = 6  
      - nums[1..3] = 2+3+1 = 6  
      - nums[4..5] = 4+2   = 6  
 
    **힌트**
    - 이중 for 루프로 모든 시작·끝 인덱스 조합을 탐색하세요.
    - 내장 함수 sum(nums[i:j+1])을 활용하세요.
    - 조건을 만족하는 [i, j] 쌍을 result에 append 하세요.
 
    **주의**
    - 리스트/인덱스 이외의 자료구조를 사용하지 마세요.
    - 결과 리스트의 순서는 시작 인덱스 오름차순이어야 합니다.
    """
    result = []
 
    # ===== Your code here =====
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            if sum(nums[start:end + 1]) == target_sum:
                result.append([start, end])

    # ==========================
    return result
 
 
if __name__ == "__main__":
    nums = [1, 2, 3, 1, 4, 2, 3]
    target_sum = 6
    answer = solution(nums, target_sum)
    print(answer)