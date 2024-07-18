class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        
        adjacency = [[] for _ in range(n)]
        for u,v in roads:
            adjacency[u].append(v)
            adjacency[v].append(u)
            
        m = len(targetPath)
        
        dp = [[inf]*m + [0] for _ in range(n)]        
        pred = [[-1]*m for _ in range(n)]

        for idx in range(m-1,-1,-1):
            for node in range(n):
                ans = inf
                for adj in adjacency[node]:
                    if dp[adj][idx+1] < ans:
                        ans = dp[adj][idx+1]
                        pred[node][idx] = adj
                dp[node][idx] = ans + (targetPath[idx] != names[node])
        
        res = [min(range(n), key = lambda i : dp[i][0])]
        for i in range(m-1):
            res.append(pred[res[-1]][i])
            
        return res
    
                
            
                