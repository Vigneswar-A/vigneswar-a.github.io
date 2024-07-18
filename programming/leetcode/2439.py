class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        

        finished = set()
        def dfs(startnode):
            visited = set()
            if startnode in visited:
                return -1
            dists = {}
            stack = [(startnode, 0)]
            while stack:
                node, dist = stack.pop()
                if node in finished:
                    continue
                if node in visited:
                    finished.update(visited)
                    return dist - dists[node]
                visited.add(node)
                dists[node] = dist
                if edges[node] == -1:
                    continue
                else:
                    stack.append((edges[node], dist+1))
            
            finished.update(visited)
            return -1
        
        return max(map(dfs, range(len(edges))))
                
                
        
            
            
        
        
        
        