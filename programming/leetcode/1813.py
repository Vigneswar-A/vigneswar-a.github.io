class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        
        prefix = list(accumulate(nums)) + [0]
        counts = Counter()
        res = 0
        
        l = 0
        for r in range(len(nums)):
            counts[nums[r]] += 1
            
            while counts[nums[r]] > 1:
                counts[nums[l]] -= 1
                l += 1
            
            res = max(res, prefix[r]-prefix[l-1])
            
        return res
            
            
        