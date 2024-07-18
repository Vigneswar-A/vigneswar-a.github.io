class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        MAX=sorted(nums,reverse=1)[:k]
        List=[]
        for i in nums:
            if i in MAX:
                MAX.remove(i)
                List.append(i)
                
        return List
            
            
        
        