class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 0
        while k:
            i += 1
            if n % i == 0:
                k -= 1
            if i > n:
                return -1
            
                
        return i