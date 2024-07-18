class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        res = 0
        pos = True
        for d in str(n):
            if pos:
                res += int(d)
            else:
                res -= int(d)
            pos = not pos
                
        return res
        