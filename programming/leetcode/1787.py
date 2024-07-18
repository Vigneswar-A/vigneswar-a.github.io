class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [*accumulate(nums), 0]
        res = []

        for i in range(n):
            left = (i*nums[i] - prefix[i-1])
            right = (prefix[-2]-prefix[i]) - (n-i-1)*nums[i]
            res.append(left + right)

        return res
