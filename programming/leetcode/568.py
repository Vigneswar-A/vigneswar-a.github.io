class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        
        n = len(flights)
        k = len(days[0])
        
        @cache
        def dp(i=0, week=0):
            if week == k:
                return 0
            ans = 0
            for j in range(n):
                if flights[i][j]:
                    ans = max(ans, dp(j, week+1)+days[j][week])
            return max(ans, dp(i, week+1)+days[i][week])
        
        return dp()
                
                
            
        