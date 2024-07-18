class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1:
            return 1
        digits = []
        for i in range(9, 1, -1):
            while num%i == 0:
                digits.append(i)
                num //= i
           
        
        if num != 1:
            return 0
        else:
            res = int("".join(sorted(map(str, digits))))
            return res if res <= 2**31 - 1 else 0
        
                
                
                
                
                        
                
        