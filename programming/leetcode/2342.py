class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = sum(nums)
        left = 0
        res = 0
        min_diff = inf
        for i in range(n):
            left += nums[i]
            diff = abs(left//(i+1) - (((total-left)//(n-i-1)) if n-i-1 else 0))
            if diff < min_diff:
                res = i
                min_diff = diff
                
        return res
            