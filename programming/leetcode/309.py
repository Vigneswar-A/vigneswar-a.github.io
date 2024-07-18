class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        last_day = len(prices)
        
        @cache
        def dp(day=0, hold=0, cooldown=0):
            if day == last_day:
                return 0
            
            if cooldown:
                return dp(day+1, 0, 0)
            
            if hold:
                return max(dp(day+1, 0, 1) + prices[day], dp(day+1, 1, 0))
            
            return max(dp(day+1, 1, 0)-prices[day], dp(day+1, 0, 0))
        
        return dp()