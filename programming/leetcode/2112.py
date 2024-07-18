class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        

        res = inf
        for i in range(len(nums) - k + 1):
            res = min(res, max(nums[i:i+k]) - min(nums[i:i+k]))
        return res
            
        