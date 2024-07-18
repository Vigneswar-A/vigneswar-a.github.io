class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        def place_mines(x,y):
            """
            mines means any 'O's connected to this coordinate cannot be flipped to X
            """
            board[x][y] = '*'
            for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                if 0 <= x+dx < m and 0 <= y+dy < n and board[x+dx][y+dy] == 'O':
                    place_mines(x+dx, y+dy)
                    
                    
# place mines on top and bottom borders
        for i in range(n):
            if board[0][i] == 'O':
                place_mines(0,i)
                
            if board[m-1][i] == 'O':
                place_mines(m-1,i)
                
                
# place mines on left and right borders
        for i in range(m):
            if board[i][0] == 'O':
                place_mines(i,0)
        
            if board[i][n-1] == 'O':
                place_mines(i,n-1)
                
        
# change mines to O (cannot be flipped) and O to X (flipped)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
                
        
        
                
        
                    
            
    
                    

        
                        