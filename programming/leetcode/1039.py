class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        out_degree = [0]*(n+1)
        in_degree = [0]*(n+1)

        for u,v in trust:
            out_degree[u] += 1
            in_degree[v] += 1
            
        res = None
        for i in range(n+1):
            if out_degree[i] == 0 and in_degree[i] == n-1:
                if res:
                    return -1
                res = i
                
        return res if res is not None else -1
                
        
    