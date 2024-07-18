class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r,c = len(matrix), len(matrix[0])
        dp = [[0]*c for _ in range(r)]
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if matrix[i][j] == '1':
                    dp[i][j] = (dp[i][j+1] if j+1 < c else 0) + 1
                    
         
        
        ans = 0
        for i in range(r):
            for j in range(c):
                min_len = dp[i][j]
                for h in range(i+1):
                    min_len = min(min_len, dp[i-h][j])
                    ans = max(ans,  (h+1)*min_len)
                
                
        return ans
         
   
        
               
        