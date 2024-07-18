class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res = 0
        conseq = 0
        for i in nums:
            if i == 0:
                conseq += 1
            else:
                res += conseq*(conseq+1) >> 1
                conseq = 0
                
        return res + (conseq*(conseq+1)//2)
        