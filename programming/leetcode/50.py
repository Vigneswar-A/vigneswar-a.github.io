class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
            
        res = x
        extra = 1
        while n > 1:
            if n%2 == 0:
                n //= 2
                res *= res
            else:
                n -= 1
                extra *= res
                
        return res*extra
                
        