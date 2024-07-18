class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
   
        n = len(grid)
        dp = [[inf]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
                 

        ans = -inf
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = min(dp[i][j], dp[i+1][j]+1, dp[i][j+1]+1)
                ans = max(ans, dp[i][j])

        return ans if ans and ans != inf else -1
                   


            

                
        
        
            
        