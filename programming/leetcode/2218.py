class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        
        adj = defaultdict(set)
        
        for u,v in corridors:
            adj[u].add(v)
            adj[v].add(u)
            
        pairs = set()
        for i in range(n):
            adjs = list(adj[i])
            for j in range(len(adjs)):
                for k in range(j+1, len(adjs)):
                    if adjs[j] in adj[adjs[k]]:
                        pairs.add(frozenset({i, adjs[j], adjs[k]}))
                        
        return len(pairs)
                        
        
        