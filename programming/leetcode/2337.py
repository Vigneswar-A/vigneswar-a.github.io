class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        res = -inf
        for i in range(len(number)):
            if number[i] == digit:
                res = max(res, int(number[:i] + number[i+1:]))
        
        return str(res)
            
                
        