class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        res = 0
        for c,k in groupby(colors):
            val =  max(sum(1 for i in k)-2, 0)
            res += (val if c == 'A' else -val)
            
        return res > 0
        