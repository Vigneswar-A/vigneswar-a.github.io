class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        column=set()
        row=set(min(row) for row in matrix)
        
        for i in range(n):
            maxvalue=0            
            for j in range(m):
                maxvalue=matrix[j][i] if matrix[j][i]>maxvalue else maxvalue            
            column.add(maxvalue)
        
        return row&column
        
        
        
        
        
        