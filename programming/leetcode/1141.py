class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        
        total=0
        count=0
        
        for i in weight:
            total+=i
            if total>5000:
                break
            count+=1
                
        return count
        
        
        