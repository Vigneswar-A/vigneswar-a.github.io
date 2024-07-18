class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        left = 0
        right = len(nums)-2
        
        while left <= right:
            mid = left+right >> 1

            if mid%2:
                if nums[mid] == nums[mid+1]:
                    right = mid-1     
                elif nums[mid] == nums[mid-1]:
                    left = mid+1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid-1]:
                    right = mid-1     
                elif nums[mid] == nums[mid+1]:
                    left = mid+1
                else:
                    return nums[mid]
                
                
            
        return nums[left]
        