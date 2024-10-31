class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        ones = 0
        
        for c in s:
            if c == '1':
                ones += 1
            else:
                res += ones
        return res
            
        