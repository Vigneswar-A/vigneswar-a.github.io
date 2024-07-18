class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for i,c in groupby(s):
            n = sum(1 for _ in c)
            res = (res + n*(n+1)//2)%(10**9+7)
            
        return res