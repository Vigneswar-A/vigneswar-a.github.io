class Solution:
    def maxOperations(self, s: str) -> int:
        
        res = 0
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0' and s[i-1] == '1':
                count += 1
            if s[i] == '1':
                res += count
                
        return res