class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = len(days)
        validity = [1, 7, 30]
        
        @cache
        def dp(idx=0, valid=0):

            if idx == last_day:
                return 0
            
            if days[idx] < valid:
                return dp(idx+1, valid)
            
            res = float('inf')
            
            for i in range(3):
                res = min(costs[i]+dp(idx+1, days[idx]+validity[i]), res)
                
            return res
                
            
        return dp()
        