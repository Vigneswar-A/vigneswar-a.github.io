class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pointer = 0
        non_zero_pointer = 0
        n = len(nums)
        
        while non_zero_pointer < n:
            if not nums[non_zero_pointer]:
                non_zero_pointer += 1
                continue
            
            if nums[zero_pointer] and zero_pointer < non_zero_pointer:
                zero_pointer += 1
                continue
                
            nums[zero_pointer] , nums[non_zero_pointer] = nums[non_zero_pointer] , nums[zero_pointer]
            non_zero_pointer += 1
            zero_pointer += 1
            
        
        
                
            
            
        
        