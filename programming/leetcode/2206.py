class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adjacency = defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                d = sqrt((x1-x2)**2 + (y1-y2)**2)
                if d <= r1:
                    adjacency[i].append(j)
                if d <= r2:
                    adjacency[j].append(i)
                    
        visited = set()
        def dfs(root):
            for adj in adjacency[root]:
                if adj in visited:
                    continue
                visited.add(adj)
                dfs(adj)
                if adj in visited:
                    continue
        
        res = 0
        for i in range(n):
            visited.add(i)
            dfs(i)
            res = max(res, len(visited))
            visited.clear()
            
        return res
                    
                
        