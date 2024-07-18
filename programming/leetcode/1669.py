class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        cuts = set(cuts)
        
        @cache
        def dp(left=0, right=n):
            flag = False
            ans = inf
            for cut in cuts:
                if left < cut < right:
                    flag = True
                    ans = min(ans, dp(left, cut)+dp(cut, right)+(right-left))
            return ans if flag else 0
        
        return dp()
                
            
        