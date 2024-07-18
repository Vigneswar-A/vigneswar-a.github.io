class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        res = []
        nums.append(upper+1)
        nums.insert(0,lower-1)
        
        for i in range(1,len(nums)):           
            if nums[i-1]!=nums[i]-1:
                res.append([nums[i-1]+1,nums[i]-1])
                    
        return res
                    
                    
                
                
            
            
        
                
        