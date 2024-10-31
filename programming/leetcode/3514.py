class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        link = [*range(1, n)]+[-1]
        res = []
        dist = n-1
        for u,v in queries:
            if link[u] != -1 and link[u] < v:
                curr = link[u]
                while curr != v:
                    link[curr], curr = -1, link[curr]
                    dist -= 1
                link[u] = v
            res.append(dist)
        return res
            
                
            
            
            
        