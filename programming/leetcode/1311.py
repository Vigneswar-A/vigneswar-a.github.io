class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        def ismagicsquare(i, j, length):
            sums = set()
            diag = antidiag = 0
            for k in range(length):
                diag += grid[i+k][j+k]
                antidiag += grid[i+k][j+length-1-k]
                sums.add(sum(grid[i+z][j+k] for z in range(length)))
                sums.add(sum(grid[i+k][j:j+length]))
            sums.add(diag)
            sums.add(antidiag)
            return len(sums) == 1

        for i in range(m):
            for j in range(n):
                for length in range(min(m-i, n-j)+1):
                    if ismagicsquare(i, j, length):
                        res = max(res, length)
        return res
                        
                        
        