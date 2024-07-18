class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if 0 <= i+dx < len(mat) and 0 <= j+dy < len(mat[0])and mat[i+dx][j+dy] > mat[i][j]:
                        break
                else:
                    return (i, j)
                        
        