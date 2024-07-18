class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.insert(bisect.bisect_right(intervals, newInterval), newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][-1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [min(interval[0], res[-1][0]), max(interval[1], res[-1][1])]
        return res

        
