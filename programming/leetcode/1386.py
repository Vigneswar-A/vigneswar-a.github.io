class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        num_rows, num_cols = len(grid), len(grid[0])

        for _ in range(k):

            previous = grid[-1][-1]
            for row in range(num_rows):
                for col in range(num_cols):
                    temp = grid[row][col]
                    grid[row][col] = previous
                    previous = temp
        return grid