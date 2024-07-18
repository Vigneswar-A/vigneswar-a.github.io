class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        
        @cache
        def dp(i = 0):
            if i == n:
                return 0
            
            res = 0
            largest = 0
            for j in range(i, min(i+k, n)):
                largest = max(largest, arr[j])
                res = max(res, dp(j+1)+(j-i+1)*largest)
            return res
        
        return dp()
                
        