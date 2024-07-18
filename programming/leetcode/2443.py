
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        b, c, d = 1, 0, 0

        for i in range(n-1,-1,-1):
            a = 0
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                a = c
            if (not a) and (i+2 < len(nums)) and (nums[i] == nums[i+1] == nums[i+2] or nums[i]+1 == nums[i+1] == nums[i+2]-1):
                a = d
            d = c
            c = b
            b = a
 
        return a
