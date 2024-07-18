class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_,max_ = min(nums),max(nums)
        return sum(min_<n<max_ for n in nums)
        