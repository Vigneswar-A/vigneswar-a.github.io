class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        visited = set()
        m,n = len(grid1), len(grid1[0])
        def dfs(x, y):
            
            if (x,y) in visited:
                return 0
            
            is_sub = 1
            stack = [(x,y)]
            
            while stack:
                x,y = stack.pop()
                
                if (x,y) in visited:
                    continue
                    
                visited.add((x, y))
                if grid1[x][y] != grid2[x][y]:
                    is_sub = 0
                    
                for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    if 0 <= x+dx < m and 0 <= y+dy < n and grid2[x+dx][y+dy] == 1:
                        stack.append((x+dx,y+dy))
                        
            return is_sub
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    ans += dfs(i, j)
        
        return ans
                    
                
        