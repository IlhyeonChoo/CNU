def solution(nums):
    """
    **문제**
    정수 리스트 nums가 주어질 때,
    가장 긴 '순증가(strictly increasing)' 부분 수열의 길이를 반환하세요.
    (부분 수열은 연속하지 않아도 됩니다.)
 
    **예시**
    입력: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    출력: 4
      - 가능한 LIS 예시: [2, 3, 7, 18] 또는 [2, 5, 7, 101]
 
    **힌트**
    - dp 리스트를 만들어 dp[i] = nums[i]로 끝나는 LIS의 길이를 저장하세요.
    - 초기값: dp = [1] * len(nums)  (자기 자신만으로 길이 1)
    - 이중 for 루프: i를 0..n-1, j를 0..i-1 순으로 탐색하세요.
      - nums[j] < nums[i] 이면 dp[i] = max(dp[i], dp[j] + 1)
    - 최종 답은 max(dp) 입니다.
 
    **주의**
    - O(n²) DP 풀이로 구현하세요 (이진 탐색 최적화 불필요).
    - 리스트/인덱스 이외의 자료구조를 사용하지 마세요.
    """
    if not nums:
        return 0
 
    n = len(nums)
    dp = [1] * n
 
    # ===== Your code here =====
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # ==========================
    return max(dp)
 
 
if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    answer = solution(nums)
    print(answer)