class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        counts = Counter()
        res = 0
        for right in range(n):
            counts[nums[right]] += 1
            while counts[0] > 1:
                counts[nums[left]] -= 1
                left += 1
                
            res = max(res, right-left)
            
        return res
            