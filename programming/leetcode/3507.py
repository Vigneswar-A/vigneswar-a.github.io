class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        
        table = [1]*(isqrt(r)+1)
        res = r-l+1
        for i in range(2, isqrt(r)+1):
            if table[i]:
                for j in range(i*i, isqrt(r)+1, i):
                    table[j] = 0
            if table[i] and l <= i**2:
                res -= 1

        return res
                    
                
        
        