class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n - 1, 0 , -1):
            if nums[i] > nums[i - 1]:
                break
        else:
            nums.sort()
            return
                
        next_bigger = i 
        
        for j in range(i , n):
            if nums[next_bigger] >= nums[j] > nums[i - 1]:
                next_bigger = j
    
        nums[i - 1] , nums[next_bigger] = nums[next_bigger] , nums[i - 1]
        nums[i:] = sorted(nums[i:])
                
            
    
        
        