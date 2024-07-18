class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        return bisect.bisect(range(1, m*n), 0, key=lambda x : sum(min(n, x//i) for i in range(1, m+1)) >= k)+1
    
    