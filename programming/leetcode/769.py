class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        
        
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)] #up, left, down, right
        mines = set((i,j) for i,j in mines)
        
        for i in range(n):
            for j in range(n):
                if i and (i-1, j) not in mines:
                    dp[i][j][0] = dp[i-1][j][0] + 1
                if j and (i, j-1) not in mines:
                    dp[i][j][1] = dp[i][j-1][1] + 1
                    
          
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < n and ((i+1, j) not in mines):
                    dp[i][j][2] = dp[i+1][j][2] + 1
                if j+1 < n and ((i, j+1) not in mines):
                    dp[i][j][3] = dp[i][j+1][3] + 1

        ans = 0
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    ans = max(ans, min(dp[i][j]) + 1)
                
        return ans