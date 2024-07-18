class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        end = len(word)
        n,m = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def backtrack(x,y,nxt=1):
            if nxt == end:   
                return True 

            board[x][y] = '_'
            for dx,dy in directions:
                if not (0 <= x+dx < n and 0 <= y+dy < m):
                    continue
                if board[x+dx][y+dy] == word[nxt] and backtrack(x+dx,y+dy,nxt+1):
                    return True
                    
            board[x][y] = word[nxt-1]
                       
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backtrack(i,j):
                    return True

        return False
                    
                        
                
            
                
            
            