class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def dp(s, e, player):
            if e < s:
                return 0
            
            if player:
                return max(dp(s+1 , e, not player)+nums[s] , dp(s , e-1, not player)+nums[e])
            
            return min(dp(s+1 , e, not player)-nums[s] , dp(s , e-1, not player)-nums[e])
                
        return dp(0, len(nums)-1, 1) >= 0
            