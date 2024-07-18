class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        
        total = sum(nums)
        currsum = 0
        res = -inf
        for num in nums:
            currsum += num
            res = max(res, currsum, total-currsum+num)
            
        return res
        