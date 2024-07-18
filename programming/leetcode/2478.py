class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        res = 0
        mask = 0
        l = 0
        for r in range(len(nums)):
            while mask&nums[r] != 0:
                mask ^= (mask&nums[l])
                l += 1
            mask |= nums[r]
            res = max(res, r-l+1)
            
        return res
                
            
        