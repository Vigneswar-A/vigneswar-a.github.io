class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        prev = ''
        for c in s:
            if c.isdigit():
                c = chr(ord(prev) + int(c))
            res += c
            prev = c
            
        return res
        