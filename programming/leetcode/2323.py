class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
    
        res = 0
        for i,j in zip(f"{bin(start)[2:]:0>30}", f"{bin(goal)[2:]:0>30}"):
            if i != j:
                res += 1
                
        return res
                
        