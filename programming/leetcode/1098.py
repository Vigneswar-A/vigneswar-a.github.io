from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        nums=Counter(nums+[-1])
        return max(i for i in nums if nums[i]==1)
        