class Solution:
    def countDigits(self, num: int) -> int:
        
        res = 0
        for d in str(num):
            if num%int(d) == 0:
                res += 1
                
        return res
        