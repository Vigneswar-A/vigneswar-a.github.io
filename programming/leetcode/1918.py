class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        i = j = k
        min_val = res = nums[k]
        while i >= 0 and j < len(nums):
            res = max(res, min_val*(j-i+1))
            if j+1 >= len(nums) or (i-1 >= 0 and nums[i-1] > nums[j+1]):
                i -= 1
            else:
                j += 1
            min_val = min(min_val, nums[i], nums[j])
            
        return res
            
                
            
        