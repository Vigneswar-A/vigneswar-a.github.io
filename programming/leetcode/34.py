class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return -1,-1
           
        
        curr = mid
        while curr < len(nums) and nums[curr] == target:
            curr += 1
        last = curr-1
        
        curr = mid
        while curr >= 0 and nums[curr] == target:
            curr -= 1
        first = curr+1
        
        return first , last
                
            
        