class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                right_bound = bisect.bisect_left(nums, nums[i]+nums[j])
                res += max(0, right_bound-j-1)
                
        return res