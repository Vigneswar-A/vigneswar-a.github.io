class Solution:
    def countDistinct(self, s: str) -> int:
        return len(set(s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)))
        