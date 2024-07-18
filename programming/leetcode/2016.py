class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort(reverse=1)
        res = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                res += i

        return res
            
