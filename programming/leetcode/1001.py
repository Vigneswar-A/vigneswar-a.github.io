class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n)>1:
                return n
