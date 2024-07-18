class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def dp(idx=0, prev_color=-1, neis=0):
            if idx == m and neis == target:
                return 0
            elif idx == m or neis > target:
                return inf

            if houses[idx] == 0:
                res = inf
                for color in range(1, n+1):
                    res = min(res, dp(idx+1, color, neis + (color != prev_color)) + cost[idx][color-1])
                return res
            else:
                return dp(idx+1, houses[idx], neis + (prev_color != houses[idx]))
            
        ans = dp()
        return ans if ans != inf else -1
                    
                