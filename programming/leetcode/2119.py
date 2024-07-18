class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        
        prefix = []
        dups = 0
        seen = set()
        for i in nums:
            if i in seen:
                dups += 1
            seen.add(i)
            prefix.append(dups)
        res = inf
        for i in range(len(nums)):
            j = bisect.bisect(nums, nums[i]+len(nums)-1)
            res = min(res, len(nums)-j+i+prefix[j-1]-prefix[i])
            
        return res