class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        res = 0
        for subset in range(1 << len(nums)):
            or_value = reduce(int.__or__, (nums[i] for i in range(len(nums)) if subset&(1 << i)), 0)
            if or_value > max_or_value:
                res = 1
                max_or_value = or_value
            elif or_value == max_or_value:
                res += 1
                
        return res
            
        