class Solution:
    def minOperations(self, k: int) -> int:
        return isqrt(k)-1+ceil(k/isqrt(k)-1)
   
        