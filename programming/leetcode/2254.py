class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        seenr = [False] * n
        seenc = [False] * n
        
        for i in range(n):
            for j in range(n):
                seenr[matrix[i][j]-1] = True
                seenc[matrix[j][i]-1] = True
            if not (all(seenr) and all(seenc)):
                return False
            
            seenr = [False] * n
            seenc = [False] * n
            
        return True
            
            
            
        