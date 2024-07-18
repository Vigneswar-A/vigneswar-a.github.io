class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=1)
        for i in range(len(nums)+1):
            if sum(nums[:i])>sum(nums[i:]):
                return nums[:i]
        