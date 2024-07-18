class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        suffix = list(accumulate(nums[::-1], int.__and__))[::-1]
        

        val = nums[0]
        res = 0
        for i in range(len(nums)-1):
            val &= nums[i]
            if val == 0 and suffix[i+1] == 0:
                res += 1
                val = nums[i+1]
                
        return res+1
                
        

        
        