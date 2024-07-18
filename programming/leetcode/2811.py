class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        i = 1
        res = set()
        while i and len(res) < n:
            if k-i not in res:
                res.add(i)
            i += 1
            
        return sum(res)
            
            
        