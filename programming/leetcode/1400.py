class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        matrix=[[None]*3 for _ in range(3)]
        
        for i in range(len(moves)):
            matrix[moves[i][0]][moves[i][1]]="A" if i%2==0 else "B"
        
        if matrix[0][0]==matrix[1][1]==matrix[2][2]!=None:return matrix[0][0]     
        if matrix[0][2]==matrix[1][1]==matrix[2][0]!=None:return matrix[0][2]
        if matrix[0][0]==matrix[1][0]==matrix[2][0]!=None:return matrix[0][0]    
        if matrix[0][1]==matrix[1][1]==matrix[2][1]!=None:return matrix[0][1]
        if matrix[0][2]==matrix[1][2]==matrix[2][2]!=None:return matrix[0][2]       
        if matrix[0][0]==matrix[0][1]==matrix[0][2]!=None:return matrix[0][0]
        if matrix[1][0]==matrix[1][1]==matrix[1][2]!=None:return matrix[1][0]
        if matrix[2][0]==matrix[2][1]==matrix[2][2]!=None:return matrix[2][0]
        
        return "Pending" if len(moves)<9 else "Draw"
        
        
        
    
         
        