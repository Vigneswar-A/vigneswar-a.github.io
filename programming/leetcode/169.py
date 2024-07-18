class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand=count=0
        for i in nums:
            if count==0 or cand==i:
                cand=i
                count+=1
                continue
            
            count-=1
        return cand
                
        