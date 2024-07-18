class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        rem = set(range(1, k+1))
        i = 0
        
        while rem:
            rem.discard(nums.pop())
            i += 1
            
        return i
            
        
        