class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ancestors = [set() for _ in range(n)]
        
        degree = [0] * n
        adjacency = [[] for _ in range(n)]
        for u,v in edges:
            adjacency[u].append(v)
            degree[v] += 1
            
        queue = deque([i for i in range(n) if degree[i] == 0])
        while queue:
            node = queue.popleft()
            for adj in adjacency[node]:
                ancestors[adj].update(ancestors[node]|{node})
                degree[adj] -= 1
                if degree[adj] == 0:
                    queue.append(adj)
                    
        return list(map(sorted, ancestors))
                
            
        
        