class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        @cache
        def dp(idx = 0 , prev = None , inc = None):
            if idx == len(nums):
                return 0
            
            if prev is None:
                return max(1+dp(idx+1 , nums[idx] , True), 1+dp(idx+1 , nums[idx], False), dp(idx+1 , None , None))
            
            if inc and nums[idx] > prev:
                return max(1+dp(idx+1, nums[idx], False), dp(idx+1, prev, True))
            
            if not inc and nums[idx] < prev:
                return max(1+dp(idx+1, nums[idx], True), dp(idx+1 , prev , False))
            
            return 0
        
        return dp()
                         