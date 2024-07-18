class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        
        res = 1
        MOD = 1000000007
        for i in range(2, n):
            res = (res*(i+1) + (1 if i%2 else -1))%MOD
        return res%MOD
                   