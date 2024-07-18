class Solution:
    def isUgly(self, n: int) -> bool:
        
        while n > 1:
            
            for divisor in (2, 3, 5):
                if n%divisor == 0:
                    n //= divisor
                    break
            else:
                return False
                    
        return n == 1
            
        