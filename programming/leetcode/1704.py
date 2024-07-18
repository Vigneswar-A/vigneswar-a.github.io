class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [sum(mat[i]) == 1 for i in range(n)]
        cols = [sum(mat[i][j] for i in range(n)) == 1 for j in range(m)]
        return sum(mat[i][j] and rows[i] and cols[j] for j in range(m) for i in range(n))
                                           
        
                    
        
        