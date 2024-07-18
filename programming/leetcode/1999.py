class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        one_max = zero_max = 0
        for k,v in groupby(s):
            if k == '0':
                zero_max = max(zero_max, sum(1 for _ in v))
            else:
                one_max = max(one_max, sum(1 for _ in v))
                
        return one_max > zero_max
            
        