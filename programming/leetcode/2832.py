class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        
        counts = Counter()
        left = 0
        res = 0
        max_count = 0
        for i in range(len(nums)):
            counts[nums[i]] += 1
            max_count = max(max_count, counts[nums[i]])
            while (i-left+1)-max_count> k:
                counts[nums[left]] -= 1
                left += 1
            res = max(res, max_count)
            
        return res
            
            