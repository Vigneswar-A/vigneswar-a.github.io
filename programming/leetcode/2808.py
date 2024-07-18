class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def dp(i=0, free=0):
            if i == n and free >= 0:
                return 0
            if i == n or free > n or free < -n:
                return inf
            
            return min(dp(i+1, free+min(time[i], n))+cost[i], dp(i+1, free-1))
        
        return dp()
            