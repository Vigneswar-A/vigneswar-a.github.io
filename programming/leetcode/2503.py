class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        res = 0
        for u,v in groupby(nums):
            if u == k:
                res = max(res, sum(1 for _ in v))
                
        return res
                
        