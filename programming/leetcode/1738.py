class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0]*n
        for u,v in roads:
            degree[u] += 1
            degree[v] += 1
            
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
               
                ans = max(degree[i]+degree[j]-([i,j] in roads or [j,i] in roads), ans)
                print(i,j,ans)
        return ans
                
        