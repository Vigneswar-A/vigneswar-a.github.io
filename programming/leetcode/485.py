class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count=maxcount=0
        
        for i in nums:
            
            if i:
                count+=1
                continue
            
            maxcount=max(count,maxcount)
            count=0
            
        return max(count,maxcount)
        