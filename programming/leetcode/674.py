class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        maxcount=count=i=0
        i=1
        
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
            
            elif nums[i-1]>=nums[i]:
                maxcount=count+1 if count+1>maxcount else maxcount
                count=0
                
        return count+1 if count+1>maxcount else maxcount
        
            
            
                
                
            
            
        