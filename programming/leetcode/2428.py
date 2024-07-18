class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = Counter()
        cols = Counter()
        
        for i in range(len(grid)):
            row_hash = ''
            col_hash = ''
            for j in range(len(grid[0])):
                row_hash += str(grid[i][j]) + '.'
                col_hash += str(grid[j][i]) + '.'
            rows[row_hash] += 1
            cols[col_hash] += 1
            
            
        res = 0
        for hash in (rows|cols):
            res += rows[hash]*cols[hash]

        return res
            
                
        