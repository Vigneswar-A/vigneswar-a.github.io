class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m,n = len(image),len(image[0])
        seen = set()
        start_color = image[sr][sc]
        
        def bfs(x,y):
            if (x,y) in seen:
                return
            seen.add((x,y))
            for dx, dy in directions:
                if 0 <= x+dx < m and 0 <= y+dy < n and image[x+dx][y+dy] == start_color:
                    image[x+dx][y+dy] = color
                    bfs(x+dx, y+dy)

                    
        bfs(sr, sc)
        image[sr][sc] = color
        return image
        
        
            
        