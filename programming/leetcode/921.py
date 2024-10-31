class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (0,-1), (-1,0)]
        res = []
        total_nums =  rows*cols
        x, y = rStart, cStart
        d = -1
        length = 1
        while len(res) < total_nums:
            d = (d+1)%4
            dx, dy = directions[d]
            for _ in range(length):
                if 0 <= x < rows and 0 <= y < cols: 
                    res.append([x, y])
                x += dx
                y += dy
                
            d = (d+1)%4
            dx, dy = directions[d]
            for _ in range(length):
                if 0 <= x < rows and 0 <= y < cols: 
                    res.append([x, y])
                x += dx
                y += dy
                
            length += 1
            
            
        return res
            
            
        