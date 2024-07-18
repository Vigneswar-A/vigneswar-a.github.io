class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @cache
        def dp(loc=start, fuel=fuel):
            if fuel < 0:
                return 0
            
            
            ans = (loc == finish)
            for nxt in range(len(locations)):
                if nxt == loc:
                    continue
                ans += dp(nxt, fuel-abs(locations[loc]-locations[nxt]))
                
            return ans
        
        return dp()%(10**9 + 7)
                
        