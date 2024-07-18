class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def dp(left=0, right=len(nums)-3):
            
            if right - left < 0:
                return 0
            
            res = 0
            
            for i in range(left, right+1):
                res = max(res, nums[left - 1]*nums[i]*nums[right + 1]+dp(left, i-1)+dp(i+1, right))               
            return res
        
        return dp()
        