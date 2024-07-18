class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
                
        nums.sort(key = lambda i : (i == 0))
        
        return nums
                    
        