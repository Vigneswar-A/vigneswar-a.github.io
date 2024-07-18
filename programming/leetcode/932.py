class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:        
        return len(set(nums[i-1] > nums[i] for i in range(1, len(nums)) if nums[i-1]!=nums[i])) <= 1