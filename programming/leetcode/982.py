class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                res += (nums[i]-nums[i+1]+1)
                nums[i+1] = nums[i]+1
        return res
                