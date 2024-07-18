class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        @cache
        def dp(i=0):
            if i >= len(nums):
                return 0
                
            return  min(dp(i+x) for x in range(1, 4))+max(k-nums[i], 0)
        
        return min(dp(i) for i in range(3))
        