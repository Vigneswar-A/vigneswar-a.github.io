class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [Counter() for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i+1, n):
                d = nums[j] - nums[i]
                dp[j][d] = max(dp[j][d], dp[i][d] + 1)
                res = max(res, dp[j][d])

        return res+1
                
                    
                
