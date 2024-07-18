class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ran=[*range(1,n:=len(nums)+1)]
        
        output=0
        for i in nums:
            if ran[i-1]!=0:
                ran[i-1]=0
                continue
            output=i
                
        return output,sum(ran)
                
        