class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        out_degree = [0]*n
        queue = deque([])
        terminals = set()
        
        for node in range(n):
            out_degree[node] = len(graph[node])
            if out_degree[node] == 0:
                terminals.add(node)
                queue.append(node)
            
        in_degree = [[] for _ in range(n)] 
            
        for node in range(n):
            for adj in graph[node]:
                in_degree[adj].append(node)
                         
                
        while queue:
            node = queue.popleft()
            for in_node in in_degree[node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0:
                    queue.append(in_node)
                    terminals.add(in_node)
                    
                    
        return sorted(terminals)
          
        
            
                
        
                
        