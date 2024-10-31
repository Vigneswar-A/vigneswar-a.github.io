class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        
        num_set = set(nums)
        
        res = 0
        for i in nums:
            count = 0
            while i*i in num_set:
                count += 1
                i = i*i
            res = max(res, count)
        return res+1 if res != 0 else -1
            