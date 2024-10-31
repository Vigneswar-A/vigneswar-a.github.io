class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        nums.sort()
        res = inf
        for i in range(len(nums)//2):
            res = min(res, (nums[i]+nums[-i-1])/2)
        return res
                      
        