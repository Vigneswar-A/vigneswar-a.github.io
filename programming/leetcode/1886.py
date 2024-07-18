class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        
        return bisect.bisect_left(range(1, 1000000000), key=lambda p : ((sum((n-1)//p for n in nums)) <= maxOperations), x=1) + 1
                
        