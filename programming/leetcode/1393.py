class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        n = len(piles)
        
        @cache
        def dp(i=0, k=0):
            if i == n or k == 0:
                return 0
            
            gain = 0
            ans = 0
            for j in range(len(piles[i])):
                gain += piles[i][j]
                if k-j-1 >= 0:
                    ans = max(ans, gain+dp(i+1, k-j-1))
                
            return max(ans, dp(i+1, k))
        
        return dp(0, k)
                
        