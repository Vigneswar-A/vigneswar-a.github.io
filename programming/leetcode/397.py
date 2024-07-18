class Solution:
    def integerReplacement(self, n: int) -> int:

        @lru_cache
        def backtrack(n , steps = 0):
            if n == 1:
                return steps
            elif n%2:
                return min(backtrack(n-1, steps+1), backtrack(n+1 , steps+1))       
            else:
                return backtrack(n//2, steps+1)
                    
        return backtrack(n)
        
        