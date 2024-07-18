class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        events = [*sorted(zip(startTime,endTime,profit))]
        starts = [event[0] for event in events]
        n = len(events)
        dp = [0]*(n+1)
        
        for idx in range(n-1, -1, -1):
            i = bisect.bisect_left(starts, events[idx][1])
            dp[idx] = max(dp[i]+events[idx][2], dp[idx+1])
            
        return dp[0]