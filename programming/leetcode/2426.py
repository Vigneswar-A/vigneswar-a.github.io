class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:

        last_day = len(present)
        dp = [[0] * (budget+1) for _ in range(last_day+1)] 

        for day in range(last_day-1 , -1 , -1):
            for bud in range(budget+1):
                if bud >= present[day] and future[day] > present[day]:
                    profit = future[day] - present[day]
                    dp[day][bud] = max(profit+dp[day+1][bud-present[day]] , dp[day+1][bud])
                else:
                    dp[day][bud] = dp[day+1][bud]

        return dp[0][budget]
        