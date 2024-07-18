class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        @cache
        def dp(idx=0, time=0, chance=k):
            if idx == len(events) or chance==0:
                return 0
            start,end,value = events[idx]
            if time < start:
                return max(dp(idx+1, end, chance-1)+value, dp(idx+1, time, chance))
            return dp(idx+1, time, chance)
        
        return dp()
            
        