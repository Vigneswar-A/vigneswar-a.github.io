class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        
        @cache
        def backtrack(idx=0, total=0):
            if idx == size:
                return target == total
            return backtrack(idx+1, total-nums[idx]) + backtrack(idx+1, total+nums[idx])
        
        res = backtrack()
        return res
                