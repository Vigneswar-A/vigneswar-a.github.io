class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for row in grid:
            row.sort(reverse=1)
        return sum(max(row) for row in zip(*grid))




        