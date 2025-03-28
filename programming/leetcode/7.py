class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = -int(str(-x)[::-1])
        else:
            res = int(str(x)[::-1])
            
        return res if -2**31 - 1 < res < 2**31 else 0
        