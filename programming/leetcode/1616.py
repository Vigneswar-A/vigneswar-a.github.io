class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return 0 if len(nums) <= 4 else min(nums[-1]-nums[3], nums[-2]-nums[2],nums[-3]-nums[1],nums[-4]-nums[0])