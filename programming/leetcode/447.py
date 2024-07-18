class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        n = len(points)
        def get_dist(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]

            return (y2-y1)**2 + (x2-x1)**2

        counts = Counter()
        for i in range(n):
            for j in range(i+1, n):
                counts[(i, get_dist(i, j))] += 1
                counts[(j, get_dist(i, j))] += 1
        return sum(count*(count-1) for count in counts.values() if count > 1)

                
