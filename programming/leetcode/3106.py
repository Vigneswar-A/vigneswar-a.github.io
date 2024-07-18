class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        dp = [[0]*(target+1) for _ in range(n+1)]
        
        for t in range(target):
            dp[0][t] = -inf
            
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            for t in range(target+1):  
                if t >= nums[i-1]:
                    dp[i][t] = max(dp[i-1][t-nums[i-1]]+1, dp[i-1][t])
                else:
                    dp[i][t] = dp[i-1][t]

        return max(dp[n][target], -1) or -1
                