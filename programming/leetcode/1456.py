class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        dp = [[inf]*n for _ in range(n)]
        
        for u,v,cost in edges:
            dp[u][v] = cost
            dp[v][u] = cost
            
        for i in range(n):
            dp[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):      
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
                    
        nei = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                if dp[i][j] <= distanceThreshold:
                    nei[i] += 1
                    nei[j] += 1

        return min(range(n-1,-1,-1), key=nei.__getitem__)
            
        