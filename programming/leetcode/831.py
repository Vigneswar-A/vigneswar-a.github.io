class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        prefix = list(accumulate(nums)) + [0]
        n = len(nums)
        
        @cache
        def dp(i = 0, k = k):
            if k == 0 and i == n:
                return 0
            elif k == 0 or i == n:
                return -inf
            res = 0
            for j in range(i, len(nums)):
                res = max(res, (prefix[j]-prefix[i-1])/(j-i+1)+dp(j+1, k-1))
            return res
                
        return dp()