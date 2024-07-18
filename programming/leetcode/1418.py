class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        total = k+1
        
        @cache
        def dp(bitmask, k=0):
            if k == total:
                return inf
            elif bitmask == 0:
                return 0
            ans = inf
            for i in range(2**n):
                if i&bitmask == i and i&bitmask:
                    ans = min(ans, max(dp(bitmask^i, k+1), sum(cookies[j] for j in range(n) if i&(1 << j))))       
            return ans
        
        bitmask = 0
        for i in range(n):
            bitmask |= (1 << i)
            
        return dp(bitmask)