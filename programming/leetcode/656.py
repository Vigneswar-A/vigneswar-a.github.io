class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        if len(coins) == 1:
            return [1]
        n = len(coins)
    
        dp = [inf]*n
        s = [0]*n
        
        dp[n-1] = 0
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, min(i+maxJump+1, n)):
                if coins[j] == -1:
                    continue
                cost = dp[j]+coins[j]
                if cost < dp[i]:
                    s[i] = j
                    dp[i] = cost
                    
        if dp[0] == inf:
            return []
        
        i = s[0]
        res = [1]
        while i != n-1:
            res.append(i+1)
            i = s[i]
        return res + [n]
            
            
        