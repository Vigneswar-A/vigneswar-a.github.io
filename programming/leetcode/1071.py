class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        tot = 0
        res = []
        
        for i in nums:
            tot = tot * 2 + i
            res.append(tot % 5 == 0)
        
        return res
            
            
        