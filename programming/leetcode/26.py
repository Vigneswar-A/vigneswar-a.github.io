class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 1
        right = 1
        
        while left < len(nums) and right < len(nums):
            while right < len(nums) and nums[left-1] == nums[right]:
                right += 1
            if right == len(nums):
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
            
        return left
        
        
            
        
        
    
        