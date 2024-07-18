class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def get_dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return max(abs(x1-x2), abs(y1-y2))

        res = 0
        for i in range(1, len(points)):
            res += get_dist(points[i-1], points[i])

        return res

