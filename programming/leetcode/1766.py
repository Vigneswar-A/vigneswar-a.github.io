class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        @cache
        def dp(i=0, d=-1):
            res = 0 if d == 1 else -inf
            for j in range(i+1, len(nums)):
                if d < 1 and nums[j] > nums[i]:
                    res = max(res, dp(j, 0)+1)
                if d >= 0 and nums[j] < nums[i]:
                    res = max(res, dp(j, 1)+1)
            return res
        
        return len(nums)-max(dp(i) for i in range(len(nums)))-1
                    