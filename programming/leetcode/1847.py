class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        max_nums = sorted(set(nums) , reverse = 1)
        i = 0
        n = len(nums)
        
        while n - nums.index(max_nums[i]) < k:
            i += 1
            
        i = nums.index(max_nums[i]) 
        return nums[i:i+k]
        
            
        
        