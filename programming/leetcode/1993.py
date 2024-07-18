class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for mask in range(2**(len(nums))):
            res += reduce(int.__xor__,(nums[i] for i in range(len(nums)) if mask&(1<<i)), 0)
        return res
            
            