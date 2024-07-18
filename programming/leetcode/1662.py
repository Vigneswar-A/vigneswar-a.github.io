class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ops = 0
        while any(nums):
            if all(i%2 == 0 for i in nums):
                nums = [num // 2 for num in nums]
                ops += 1
            else:
                for i in range(len(nums)):
                    if nums[i]%2:
                        nums[i] -= 1
                        ops += 1
                        
        return ops
            