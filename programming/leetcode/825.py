class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prev_height = sum(chain.from_iterable(grid))
        row_max = [max(i) for i in grid]
        col_max = [max(i) for i in zip(*grid)]

        return sum(min(row_max[i] , col_max[j]) for j in range(n) for i in range(n)) - prev_height
        