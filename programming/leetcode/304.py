class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = [list(accumulate(row)) + [0] for row in matrix]
    
    @lru_cache
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:  
            return sum(self.mat[row][col2] - self.mat[row][col1 - 1] for row in range(row1 , row2 + 1))
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


