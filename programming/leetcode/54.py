class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        
        visited = [[False] * n for _ in range(m)]
        x,y = (0,0)
        
        
        res = []
        direction = cycle([(1,0),(0,1),(-1,0),(0,-1)])
        dx,dy = next(direction)
        
        def inc():
            nonlocal x , y , dx , dy
            x += dx
            y += dy
            
        def dec():
            nonlocal x , y , dx , dy
            x -= dx
            y -= dy
            
        def travel():
            nonlocal x , y , dx , dy
            if not (0 <= x < n and 0 <= y < m):
                dec()
                dx,dy = next(direction)
                inc()
                
            if visited[y][x]:
                dec()
                dx,dy = next(direction)
                if visited[y + dy][x + dx]:
                    return
                inc()
                
            res.append(matrix[y][x])
            visited[y][x] = True
            inc()
            travel()
            
        travel()
        return res
            
            
                    
                
                
                    
                
                
            
                
        
            
            
        