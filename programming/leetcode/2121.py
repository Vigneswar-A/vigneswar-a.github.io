class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjecency = defaultdict(list)
        
        for i , j in edges:
            adjecency[i].append(j)
            adjecency[j].append(i)
            
        queue = deque([source])
        seen = set()
        
        while queue:
            node = queue.pop()
            if node == destination:
                return True
            
            if node in seen:
                continue
                
            seen.add(node)
            queue.extend(adjecency[node])
            
        return False
        