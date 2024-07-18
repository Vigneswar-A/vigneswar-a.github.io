class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums_count = Counter()
        prefix_sum = 0
        res = 0
        for i in nums:
            prefix_sum += i
            if prefix_sum == goal:
                res += 1
            res += sums_count[prefix_sum-goal]
            sums_count[prefix_sum] += 1
            
            
        return res