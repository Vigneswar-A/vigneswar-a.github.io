class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        minval = inf
        maxval = -inf

        for i in nums:
            minval = minval if minval < i else i
            maxval = maxval if maxval > i else i

        diff = maxval - minval

        return diff-2*k if diff > 2*k else 0