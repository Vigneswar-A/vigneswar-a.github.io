class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        # find the next higher element
        stack = []
        next_greater = [-1]*n
        for e,i in sorted((e,i) for i,e in enumerate(arr)):
            while stack and i > stack[-1]:
                next_greater[stack.pop()] = i
            stack.append(i)
               
        # find the next lower element
        stack = []
        next_lower = [-1]*n
        for e,i in sorted((-e,i) for i,e in enumerate(arr)):
            while stack and i > stack[-1]:
                next_lower[stack.pop()] = i
            stack.append(i)
            
        # dp
        dp = [[False, False] for _ in range(n+1)]
        dp[n-1][0] = dp[n-1][1] = True
        
        res = 0
        for i in range(n-2,-1,-1):
            dp[i][0] = dp[next_lower[i]][1]
            dp[i][1] = dp[next_greater[i]][0]
            res += dp[i][1]
                
        return res+1
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    