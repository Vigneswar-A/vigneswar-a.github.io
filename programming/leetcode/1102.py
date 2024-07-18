class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        vote=0
        for i in nums:
            vote+=1 if i==target else -1
        
        return vote>0
        