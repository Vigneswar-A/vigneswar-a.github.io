class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m,n = len(mat) , len(mat[0])
        
        diagonals= [[] for _ in range(m+n-1)]
        
        for i in range(m):
            for j in range(n):
                diagonals[i+n-j-1].append(mat[i][j])
            
        for diagonal in diagonals:
            diagonal.sort()
            
        diagonals = [*map(iter , diagonals)]
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = next(diagonals[i+n-j-1])
                
        return mat
                
                
        
        