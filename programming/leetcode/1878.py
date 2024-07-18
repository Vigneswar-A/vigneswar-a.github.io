class Solution:
    def check(self, nums: List[int]) -> bool:
        
        max_idx1,max_idx2 = max(range(len(nums)), key=nums.__getitem__) + 1,max(range(len(nums)-1,-1,-1), key=nums.__getitem__) + 1
        
        return nums[max_idx1:] + nums[:max_idx1] == sorted(nums) or nums[max_idx2:] + nums[:max_idx2] == sorted(nums)
       
    