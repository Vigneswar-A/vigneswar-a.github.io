class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        hashmap = defaultdict(list)
        
        for i,c in enumerate(ring):
            hashmap[c].append(i)
            
        n,m = len(ring),len(key)
        
        @cache
        def dp(i=0, j=0):
            if i == m: return 0
            ans = inf
            for nxt in hashmap[key[i]]:    # dont rotate - rotate clock wise - rotate anti clock wise
                ans = min(ans, dp(i+1, nxt) + min(abs(nxt-j), abs(n+j-nxt), abs(n-j+nxt)) + 1)
            return ans
        
        return dp()
                
            