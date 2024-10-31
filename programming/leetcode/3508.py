class Solution:
    def minChanges(self, n: int, k: int) -> int:
        
        res = 0
        for i in range(32):
            if (n&(1 << i)  != k&(1 << i)):
                if (k&(1 << i)):
                    return -1
                res += 1
        return res
            
        