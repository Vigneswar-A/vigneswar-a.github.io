class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        upper = 1000000000000000001
        def todecimal(length, base):
           
            res = 0
            x = 1
            for _ in range(length):
                res += x
                x *= base
                if res > n:
                    return res
               
               
            
            return res
        
        for length in range(100, 1, -1):
            j = bisect.bisect_left(range(2, upper), n, key = partial(todecimal, length))+2
            
            
            
            
            if todecimal(length, j) == n:
                return str(j)
            
        
                
                
                
                
            
            
            