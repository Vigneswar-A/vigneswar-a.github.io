class Solution:
    def baseNeg2(self, n: int) -> str:
        
        res = ''
        i = 1
        while n:
            if n%(2**i):
                res = '1'+res
                n -= ((-2)**(i-1))
            else:
                res = '0'+res
            i += 1

        return res or '0'
        
            
            
            