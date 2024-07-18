class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = set()
        def backtrack(n=0):
            if n > high:
                return 
            elif n and n >= low:
                res.add(n)

            if n%10 < 9:
                backtrack(n*10+n%10+1)
                
        [backtrack(i) for i in range(10)]
        return sorted(res)
                
            