class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r - 2:
            if nums[l] == nums[l + 1] == nums[l + 2]:
                nums.pop(l + 2)
                r -= 1
            else:
                l += 1
                
        
            
            
                
        