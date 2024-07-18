class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adjacency = defaultdict(list)
        for u,v in connections:
            adjacency[u].append((v, 1))
            adjacency[v].append((u, 0))
            
        stack = [0]
        visited = set()
        res = 0
        while stack:
            node = stack.pop()
            visited.add(node)
            for adj,cost in adjacency[node]:
                if adj not in visited:
                    stack.append(adj)
                    res += cost
                    
        return res
                    
                