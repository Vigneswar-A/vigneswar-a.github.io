class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)
        if nums[-2] > nums[-1]:
            return nums[-1]
        x = nums[0]
        
        left,right = 1,len(nums)-1
        
        while left < right:
            
            mid = left + right >> 1
            
            if nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            
            if nums[mid] < x:
                right = mid
                
            else:
                left = mid + 1
                
        return nums[0]
                
                
        