class Solution:
    def countTriples(self, n: int) -> int:
        
        n += 1
        count = 0
        
        for a in range(1, n):
            for b in range(1, n):
                if int(sqrt(a**2 + b**2)) == sqrt(a**2 + b**2) <= n-1:
                    count += 1
                    
        return count
        