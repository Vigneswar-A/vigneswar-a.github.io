class Solution:
    def maximumGap(self, nums: List[int]) -> int:        
        difference=0
        nums.sort()        
        for i in range(len(nums)-1):difference=max(nums[i+1]-nums[i],difference)              
        return difference
    
    
            
        