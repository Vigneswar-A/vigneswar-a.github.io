class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        res = -1
        for i in range(len(nums)):
            total += nums[i]
            if total > 2*nums[i] and i >= 2:
                res = max(res, total)
            
            
        return res
            
            
            