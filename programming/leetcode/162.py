class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return nums.index(max(nums))
        
        left = 0
        right = len(nums)-1
        
        while left+1 < right:
            
            mid = left+right >> 1
            
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                left = mid
            
            else:
                right = mid
                
        return nums.index(max(nums))
                
        
            
        