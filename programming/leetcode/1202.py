class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        
        """
        @cache
        def dp(i=0, j=len(arr)-1):
            
            if i == j:
                return 1
            
            res = float('inf')
            
            if arr[i] == arr[j]:
                res = min(res, i+1 == j or dp(i+1, j-1))
                
            for k in range(i, j):             
                res = min(res, dp(i, k)+dp(k+1, j))      
                
            return res
        
        return dp()
        """
    
        n = len(arr)+1
        dp = [[inf] * n for _ in range(n)]
        
        
        for i in range(n-2, -1, -1):
            for j in range(n-1):
                if i == j:
                    dp[i][j] = 1
                    
                if arr[i] == arr[j]:
                    dp[i][j] = min(dp[i][j], int(i+1 == j) or dp[i+1][j-1])  
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

        return dp[0][n-2]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
        