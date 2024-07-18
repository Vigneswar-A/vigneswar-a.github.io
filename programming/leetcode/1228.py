class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        
        @cache
        def dp(i, j):
            if i == j:
                return 0       
            ans = inf
            for k in range(i, j):
                ans = min(ans, dp(i, k) + dp(k+1, j) + max(arr[i:k+1]) * max(arr[k+1:j+1]))
            return ans
        
        return dp(0, len(arr)-1)
                