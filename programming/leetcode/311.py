class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m = len(mat1)
        n = len(mat2[0])
        k = len(mat1[0])
        
        res = [[0]*n for _ in range(m)]
        
        for r in range(m):
            for c in range(k):
                if mat1[r][c] == 0:
                    continue
                for i in range(n):
                    res[r][i] += mat1[r][c] * mat2[c][i]
        
        return res
        