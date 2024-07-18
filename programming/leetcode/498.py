class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = [[] for _ in range(m + n - 1)]
        
        for i in range(m):
            for j in range(n):
                res[i+j].append(mat[i][j])
                
        for i in range(0 , m + n - 1 , 2):
            res[i].reverse()
                
        return chain.from_iterable(res)