class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        m = len(rides)
        for ride in rides:
            start,end,tip = ride
            ride[2] += end-start
            
        rides.sort(key=lambda arr : (arr[1], -arr[2], arr[1]))
        dp = [0]*(n+1)
        m = len(rides)
        i = 0
        for point in range(n+1):   
            if i < m and rides[i][1] > point:
                dp[point] = dp[point-1]
                continue
                
            if i == m:
                return dp[point-1]
        
            dp[point] = dp[point-1]
            while i < m and rides[i][1] == point:
                start, end, cost = rides[i]
                dp[point] = max(dp[start]+cost, dp[end])
                i += 1
            
        return dp[n]
                
            
            
            
            
            