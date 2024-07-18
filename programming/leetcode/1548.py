class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count=float('inf')
        
        for i in nums:
            if not i:
                count+=1
                continue
                
            if count<k:return 
            count=0
            
        return 1
            
        