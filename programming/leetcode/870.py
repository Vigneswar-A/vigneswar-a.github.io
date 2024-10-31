class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if i+2 < m and j+2 < n:
                    sums = set()
                    for k in range(3):
                        sums.add(grid[i][j+k]+grid[i+1][j+k]+grid[i+2][j+k])
                        sums.add(grid[i+k][j]+grid[i+k][j+1]+grid[i+k][j+2])
                    sums.add(grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2])
                    sums.add(grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j])
                    if len(sums) == 1 and set(grid[i+x][j+y] for x in range(3) for y in range(3)) == set(range(1, 10)):
                        res += 1
                        
        return res
                        
                    
                