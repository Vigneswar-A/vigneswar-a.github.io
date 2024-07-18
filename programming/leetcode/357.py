class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        seen = set()
        def backtrack(n):
            if len(seen) == n:
                return 1
            
            res = 0
            for i in range(10):
                if not seen and i == 0:
                    continue
                if i in seen:
                    continue
                seen.add(i)
                res += backtrack(n)
                seen.remove(i)
                
            return res

        
        return 1+sum(backtrack(i) for i in range(1,n+1))
                    
                    
            
                
            
            
