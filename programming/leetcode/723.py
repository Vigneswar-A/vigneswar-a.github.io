class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        m = len(board)
        n = len(board[0])
        flag = True
        
        while flag:
            to_remove = set()
            #find candies to crush
            for i in range(m):
                for j in range(n):
                    if j < n-2 and board[i][j] == board[i][j+1] == board[i][j+2] != 0:
                        to_remove.add((i, j))
                        to_remove.add((i, j+1))
                        to_remove.add((i, j+2))
                    if i < m-2 and board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                        to_remove.add((i, j))
                        to_remove.add((i+1, j))
                        to_remove.add((i+2, j))

            if not to_remove:
                flag = False
                
            #crush
            for x,y in to_remove:
                board[x][y] = 0
                
            #gravity
            for i in range(m-2,-1,-1):
                for j in range(n):
                    k = i
                    while k < m-1 and board[k][j] and board[k+1][j] == 0:
                        board[k+1][j] = board[k][j]
                        board[k][j] = 0
                        k += 1
        return board
                        
            
                
                
                    
        