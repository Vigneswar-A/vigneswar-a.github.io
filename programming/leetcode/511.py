class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #if there is no edge source has to be destination
        if not edges:
            return source == destination
        
                
        adjecency = [[] for _ in range(n)] 
        is_reached = [False] * n #is it possible to reach destination from current point
        loop = set()
        
        for u , v in edges:
            if u == v:
                loop.add(u)
            adjecency[u].append(v) 
        
        #if destination has branches then its a false
        if adjecency[destination]:
            return False
        
        stack = [([] , source)]
        seen = set()
        
        while stack:
            path , node = stack.pop()
            
            if node in loop:
                return False
            
            if node == destination:            
                for point in path:
                    is_reached[point] = True
                    continue
                    
            elif node in seen:
                if is_reached[node]:
                    for point in path:
                        is_reached[point] = True                   
                continue
            
            seen.add(node)

            is_reached[node] = False
            
            
            path.append(node)
            
            stack.extend((path[:], child) for child in adjecency[node])
            path.pop()
            
        return sum(is_reached) == len(seen) - 1
        
            
        
            
            
            
        
        