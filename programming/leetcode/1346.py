class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k%2:
            return -1
        if k <= 1:
            return nums[k]
        if k == 2:
            return max(nums[0], nums[2])
        return max([max(nums[:k-1], default=-1), nums[k] if k < len(nums) else 0])