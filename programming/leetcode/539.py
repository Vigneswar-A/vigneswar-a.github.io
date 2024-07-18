class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def mins(hr, min):
            return hr*60 + min - 12*60

        times = sorted(mins(*map(int, time.split(':'))) for time in timePoints)

        res = inf
        for i in range(len(times)):
            res = min(res, (1440-abs(times[i-1]-times[i]))%1440, abs(times[i-1]-times[i]))

        return res

        