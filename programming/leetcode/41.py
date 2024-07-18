class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == [1]: return 2
        nums.append(0)
        
        for i in range(len(nums)):
            if 1 <= int(nums[i]) < len(nums):
                h = int(nums[i])
                nums[h] = str(nums[h])
                
        
        for i in range(len(nums)):
            if isinstance(nums[i], int) and i:
                return i
            
        return i+1
            
        