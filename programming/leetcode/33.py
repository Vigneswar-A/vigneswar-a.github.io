class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left+right >> 1
            
            if nums[mid] > nums[-1]:
                left = mid+1
            else:
                right = mid-1

        i = left
        if nums[i] <= target <= nums[-1]:
            left = i
            right = len(nums)-1
        else:
            left = 0
            right = i
                
        while left <= right:
            mid = left+right >> 1
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return -1