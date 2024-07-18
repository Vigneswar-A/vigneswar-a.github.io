class Player:
    def __init__(self , size):
        self.row = [0] * size
        self.col = [0] * size
        self.diag = 0
        self.antidiag = 0
        
class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.players = {1 : Player(n) , 2 : Player(n)}
        
    def move(self, row: int, col: int, player: int) -> int:
        self.players[player].row[row] += 1
        self.players[player].col[col] += 1
        
        if row == col:
            self.players[player].diag += 1
            
        if row + col + 1 == self.size:
            self.players[player].antidiag += 1
            
        if self.players[player].row[row] == self.size or self.players[player].col[col] == self.size or\
        self.players[player].diag == self.size or self.players[player].antidiag == self.size:
            return player
        
        return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)