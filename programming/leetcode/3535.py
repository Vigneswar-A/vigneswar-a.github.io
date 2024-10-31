class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        
        @cache
        def dp(i, p1, p2):
            if i == len(nums):
                return 1
            res = 0
            for j in range(nums[i]+1):
                if j >= p1 and nums[i]-j <= p2:
                    res += dp(i+1, j, nums[i]-j)
            return res
        
        return dp(0, -inf, inf)%1000000007
        