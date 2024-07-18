class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zerocoordinates=[]
        for x in range(r:=len(matrix)):
            for y in range(c:=len(matrix[0])):
                if matrix[x][y]==0:
                    zerocoordinates.append((x,y))
                    
        for x,y in zerocoordinates:
            matrix[x]=[0]*c
            for col in range(r):
                matrix[col][y]=0
        
                
                
                    
                
                    
        