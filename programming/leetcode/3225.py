class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = Counter()
        res = 0
        left = 0
        for right in range(len(nums)):
            counts[nums[right]] += 1
            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1
            res = max(res, right-left+1)               
        return res
                
            