class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        
        m,n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)] # (0 count , 1 count)

        dp[0][0].add((int(grid[0][0]==0), int(grid[0][0]==1)))
        

        for i in range(m):
            for j in range(n):
                if i:
                    dp[i][j].update({(x+(grid[i][j]==0), y+(grid[i][j]==1)) for x,y in dp[i-1][j]})
                if j:
                    dp[i][j].update({(x+(grid[i][j]==0), y+(grid[i][j]==1)) for x,y in dp[i][j-1]})
                    
        
        
        return any(zero_count == one_count for zero_count, one_count in dp[-1][-1])
                    
                    

                    