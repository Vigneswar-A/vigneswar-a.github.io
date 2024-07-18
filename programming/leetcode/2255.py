class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        counts = {0:nums.count(0)}
        counts[1] = len(nums)-counts[0]
        
        res = inf
        for num in [0,1]:
            window = counts[num]
            swaps = 0
            for i in range(window):
                swaps += (nums[i]!=num)
            for i in range(window, len(nums)):
                res = min(res, swaps)
                swaps += (nums[i]!=num)-(nums[i-window]!=num)
            res = min(res, swaps)
            
        return res
        