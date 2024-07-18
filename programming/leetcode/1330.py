class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        
        for n in arr:
            
            if n-difference in dp:
                dp[n]=1+dp[n-difference]
            else:                
                dp[n]=1
            
        return max(dp.values())
            
        
            
                
        
            
        