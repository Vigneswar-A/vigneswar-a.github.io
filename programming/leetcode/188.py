class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @cache
        def dp(day=0, hold=False, k=k):
            if day == len(prices) or k == 0:
                return 0
            if not hold:
                return max(dp(day+1, True, k)-prices[day], dp(day+1, False, k), 0)
            
            return max(dp(day+1, False, k-1)+prices[day], dp(day+1, True, k), 0)
            
        return dp()
        