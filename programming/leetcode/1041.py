class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def get_rook_pos():
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        return i, j
                    
        rx, ry = get_rook_pos()
        res = 0
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            x, y = rx, ry
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'B':
                    break
                elif board[x][y] == 'p':
                    res += 1
                    break
                x += dx
                y += dy
                
                
        return res