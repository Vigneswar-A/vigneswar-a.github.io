class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        start = min(nums)
        
        return sorted(nums) == [*range(start, start+len(nums))]
        