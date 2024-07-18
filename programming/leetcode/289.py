class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):     
                neighbors = sum(board[i+dx][j+dy] in {-2, 1} for dx,dy in ((0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(-1,-1),(1,1)) if 0 <= i+dx < m and 0 <= j+dy < n)
                if board[i][j] and (neighbors < 2 or neighbors > 3):
                    board[i][j] = -2
                elif not board[i][j] and neighbors == 3:
                    board[i][j] = -1
                    
        for i in range(m):
            for j in range(n):
                board[i][j] = 0 if board[i][j] == -2 else 1 if board[i][j] == -1 else board[i][j]
                
            
                    