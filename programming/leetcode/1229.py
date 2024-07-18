class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adjacency_red = defaultdict(list)
        adjacency_blue = defaultdict(list)
        
        for u,v in redEdges:
            adjacency_red[u].append(v)
            
        for u,v in blueEdges:
            adjacency_blue[u].append(v)

        queue = deque([(0,'X')])
        shortest = [inf]*n
        dist = 0
        visited = set()
        
        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()
                
                if (node, color) in visited:
                    continue
                    
                visited.add((node, color))
                shortest[node] = min(dist, shortest[node])
                
                if color != 'R':
                    queue.extend(((adj,'R') for adj in adjacency_red[node]))
                
                if color != 'B':
                    queue.extend(((adj,'B') for adj in adjacency_blue[node]))
            dist += 1
                    
        return [i if i != inf else -1 for i in shortest]
                
                
            
            
            
    