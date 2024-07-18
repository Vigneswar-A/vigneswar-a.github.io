class Solution:
    def largestVariance(self, s: str) -> int:
        
        counts = Counter(s)
        letters = set(s)
        ans = 0
        
        for c1, c2 in product(letters, letters):
            if c1 == c2:
                continue
            rem = counts[c2]
            hi = lo = res = 0
            
            for c in s:
                if c == c1:
                    hi += 1
                
                if c == c2:
                    lo += 1
                    rem -= 1
                    
                if lo:
                    res = max(res, hi-lo)
                    
                if hi < lo and rem:
                    hi = lo = 0
                    
            ans = max(ans, res)
            
        return ans
                    
            
                    
                    
                
                
        