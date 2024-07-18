class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(n:=len(nums)):
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
       
        List=[]
        
        for i in range(n):
            if nums[i]>0:
                List.append(i+1)
            
        return List
                
            
       
        
        