class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        @cache
        def dp(i, j, x=-1):
            if i >= j:
                return 0
            
            res = 0
            if x == -1 or nums[i]+nums[j] == x:
                res = max(res, dp(i+1, j-1, nums[i]+nums[j])+1)
            if x == -1 or nums[i]+nums[i+1] == x:
                res = max(res, dp(i+2, j, nums[i]+nums[i+1])+1)
            if x == -1 or nums[j-1]+nums[j] == x:
                res = max(res, dp(i, j-2, nums[j-1]+nums[j])+1)
                
            return res
        
        return dp(0, len(nums)-1)
            