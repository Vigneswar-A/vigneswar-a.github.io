class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        degree = Counter()
        
        for u,v in roads:
            degree[u] += 1
            degree[v] += 1
            
            
        ranks = {node : importance for importance,node in enumerate(sorted(range(n), key=lambda i : degree[i]), 1)}

        res = 0
        for u,v in roads:
            res += ranks[u]+ranks[v]
            
        return res