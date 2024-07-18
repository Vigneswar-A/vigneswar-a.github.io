class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        
        pairs = {"0":"0", "1":"1", "8":"8", "9":"6", "6":"9"}
        res = []
        
        def backtrack(s=""):
            if len(s) == n and (s == "0" or s[0] != "0"):
                res.append(s) 
            elif len(s) < n:
                for i in pairs:
                    backtrack(i+s+pairs[i])
                
        [backtrack(i) for i in ['', '0', '1', '8']]
        
        return res
        