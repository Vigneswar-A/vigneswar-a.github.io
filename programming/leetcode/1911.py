class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
        res = ceil(abs(sum(nums)-goal)/limit)
        
        return res
        