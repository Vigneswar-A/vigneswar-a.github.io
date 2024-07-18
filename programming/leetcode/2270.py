class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if not (n := len(nums) - 1):
            return nums
        
        nums.sort()
        res = []
        
        for i in range(1 , n):
            if nums[i + 1] - nums[i] > 1 and nums[i] - nums[i - 1] > 1:
                res.append(nums[i])
         
        if nums[1] - nums[0] > 1:
            res.append(nums[0])
            
        if nums[-1] - nums[-2] > 1:
            res.append(nums[-1])
            
        return res
                