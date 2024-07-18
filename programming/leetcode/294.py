class Solution:
    def canWin(self, current: str, player=1) -> bool:
        for i in range(1, len(current)):
            if current[i-1] == current[i] == '+' and self.canWin(current[:i-1] + '--' + current[i+1:], not player) == player:
                return player
        return not player