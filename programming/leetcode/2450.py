class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] < nums[i]:
                breaks = ((nums[i] + nums[i+1] - 1) // nums[i+1])-1
                res += breaks
                nums[i] = nums[i]//(breaks+1)
        return res
                
        
                
                
        
        
        