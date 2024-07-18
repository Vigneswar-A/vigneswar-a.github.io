class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i+1])-ord(s[i])) for i in range(len(s)-1))