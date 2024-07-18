class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i in range(len(s)) if s[i] == c]
        res = []
        cr = 1
        left , right = indices[0] , indices[1] if len(indices) > 1 else float('inf')
        
        for i in range(len(s)):
            ls = abs(left - i)
            rs = abs(right - i)
            
            if ls < rs:
                res.append(ls)
            else:
                res.append(rs)
                left = right
                cr += 1
                if cr < len(indices):          
                    right = indices[cr]
        
        return res      