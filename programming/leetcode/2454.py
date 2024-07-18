class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        def get_max(i,j):
            return max(grid[i-dx][j-dy] for dx,dy in directions)
        n = len(grid)
        
        res = []
        for i in range(1 , len(grid)-1):
            temp = []
            for j in range(1 , len(grid)-1):
                temp.append(get_max(i,j))
            res.append(temp)
            
        return res
                