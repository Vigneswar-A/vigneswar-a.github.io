class Solution:
    def magicalString(self, n: int) -> int:
        
        
        res = [1, 2, 2]
        idx = 2
        while len(res) < n:
            res += res[idx]*[(3-res[-1])]
            idx += 1
            
        return res[:n].count(1)
            
        
