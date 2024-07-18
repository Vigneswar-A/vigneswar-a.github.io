class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = {-3 : 0 , -2 : 0 , -1 : 0}
        dp2 = {-3 : 0 , -2 : 0 , -1 : 0}
        
        for i,cash in enumerate(nums[:-1]):            
            dp1[i] = max(dp1[i - 1] , dp1[i - 2] + cash)
            
        for i,cash in enumerate(nums[1:]):            
            dp2[i] = max(dp2[i - 1] , dp2[i - 2] + cash)
            
        return max(dp1[i] , dp1[i-1] , dp2[i] , dp2[i-1])