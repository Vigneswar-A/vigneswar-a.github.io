class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lprefix = accumulate(nums)
        rprefix = list(accumulate(nums[::-1]))[::-1]
        
        for i , n in enumerate(rprefix):
            if n == next(lprefix):
                return i
            
        return -1                                         