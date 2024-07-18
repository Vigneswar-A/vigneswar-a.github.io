class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        counts = Counter(nums)
        
        dp = [0] * 2 * 10**4

        for i in range(2*10**4):
            dp[i] += max((counts[i]*i) + dp[i-2], dp[i-1])
            
        return max(dp)
        
        
        