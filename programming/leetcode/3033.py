class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        
        miss = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                miss.append(i)
        
        n = len(miss)
        
        @cache
        def dp(i, c):
            if i == n and c == 0:
                return 0
            elif i == n:
                return inf
            
            res = inf
            
            # operation 1
            if c: # previously we flipped one, we flip another to form a pair
                res = min(res, dp(i+1, 0)+x)
            else: # we flip this first
                res = min(res, dp(i+1, 1))
                
            if i+1 < n: # operation 2
                res = min(res, dp(i+2, c)+miss[i+1]-miss[i])
                
            return res
        
        ans = dp(0, 0)
        return ans if ans != inf else -1

              
                
         
        
        
        
            
            
        
        
            
        