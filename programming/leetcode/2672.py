class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        
        
        oneGroup = max(oneGroup, 1)
        zeroGroup = max(zeroGroup, 1)
   
        dp = [1] + [0]*(maxLength+1)
    
        for i in range(maxLength+1):
            if i >= zeroGroup: dp[i] += dp[i-zeroGroup]
            if i >= oneGroup: dp[i] += dp[i-oneGroup]

        return sum(dp[minLength:maxLength+1])%(10**9 + 7)
        