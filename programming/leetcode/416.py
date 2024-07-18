class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_%2:
            return False
        highest = sum_/2
        
        @cache
        def dp(idx=0, total=0):
            
            if idx == len(nums):
                return (total == 0)
            
            if total > highest:
                return False
                
            return dp(idx+1, total+nums[idx]) or \
                   dp(idx+1, total-nums[idx])
        
        return dp()
        