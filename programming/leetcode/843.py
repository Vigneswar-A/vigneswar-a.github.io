class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        dp = Counter()
    
        arr.sort()
        ans = 0
        
        for i in arr:
            for j in range(2, isqrt(i)+1):
                if i%j == 0:
                    dp[i] += dp[j]*dp[i//j]
                    if j != i//j: dp[i] += dp[j]*dp[i//j]
            dp[i] += 1
            ans = (ans + dp[i])%(10**9+7)
        
        return ans
        
        