class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        MAX = 100000000
        def possible(speed):
            time = 0
            for dis in dist:
                time += ceil(dis/speed)
            time += dist[-1]/speed - ceil(dist[-1]/speed)
            return (time-hour) < 0.000000001

        ans = bisect.bisect(range(1, MAX), key=possible, x = 0)+1
        
        return ans if ans != MAX else -1
                
        