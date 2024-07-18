class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        count = 0
        seen = set()
        for circle in set(map(tuple , circles)):
            X , Y , radius = circle
            for x in range(X - radius - 1, X + radius + 1):
                for y in range(Y - radius - 1, Y + radius + 1):
                    if (x , y) in seen:
                        continue
                    if (X - x)**2 + (Y - y)**2 <= radius ** 2:
                        count += 1
                        seen.add((x , y))
        return count
                    