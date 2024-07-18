class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        rows = []
        cols = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)

        row = rows[len(rows)//2]
        col = sorted(cols)[len(cols)//2]
        
        res = 0
        for r,c in zip(rows, cols):
            res += abs(r-row)+abs(c-col)
        return res
            