class Solution:
    def countAndSay(self, n: int) -> str:
        
        def get_next(s):
            res = ""
            for u,v in groupby(s):
                res += str(sum(1 for _ in v)) + str(u)
            return res
        
        temp = "1"
        for _ in range(n-1):
            temp = get_next(temp)
        return temp
                
        
        